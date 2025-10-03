from flask import Flask, jsonify, request
from src.models import Base, Track, Tag, track_tags
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

# Get password
with open("sqlalchemy_password.txt") as f:
    password = f.readline().strip()

# Create Database and tables
engine = create_engine(f"postgresql://postgres:{password}@localhost/sound_library")
Base.metadata.create_all(engine)


app = Flask(__name__)

@app.route('/api/tracks', methods=['POST', 'GET'])
def handle_tracks():
    if request.method == 'POST':
        data = request.get_json()

        with Session(engine) as session:
            track = Track(
                title = data['title'],
                artist_name = data['artist_name'],
                duration_seconds = data['duration_seconds'],
                file_path = data['file_path']
            )

            session.add(track)
            session.commit()
            session.refresh(track) # Adds id to python object (track.id)

            return jsonify({
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path
            }), 201 #201 = Created
        

    elif request.method == 'GET':
        with Session(engine) as session:
            # get track
            statement = select(Track)
            result = session.execute(statement)
            tracks = result.scalars().all()
            
            # Convert to dictionaries
            tracks_list = [{
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path
            } for track in tracks]
            return jsonify(tracks_list), 200
    
    return jsonify("Invalid request"), 400
    
    
@app.route('/api/tracks/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_track_by_id(id):
    if request.method == 'GET':
        with Session(engine) as session:
            # get track
            statement = select(Track).where(Track.id == id)
            result = session.execute(statement)
            track = result.scalar_one_or_none()

            if not track:
                return jsonify({"error": "Track not found"}), 404
            
            # Convert to dictionary
            tracks_list = {
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path}
            return jsonify(tracks_list), 200
        

    if request.method == 'PUT':
        data = request.get_json()

        with Session(engine) as session:
            # get track
            statement = select(Track).where(Track.id == id)
            result = session.execute(statement)
            track = result.scalar_one_or_none()

            if not track:
                return jsonify({"error": "Track not found"}), 404
            
            # update only what is given
            if 'title' in data:
                track.title = data['title']
            if 'artist_name' in data:
                track.artist_name = data['artist_name']
            if 'duration_seconds' in data:
                track.duration_seconds = data['duration_seconds']
            if 'file_path' in data:
                track.file_path = data['file_path']

            session.commit()
            session.refresh(track)
            
            return jsonify({
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path
            }), 200
        
    if request.method == 'DELETE':
        with Session(engine) as session:
            # get track
            statement = select(Track).where(Track.id == id)
            result = session.execute(statement)
            track = result.scalar_one_or_none()
            if track:
                session.delete(track)
                session.commit()
                return jsonify(f"Track {id}: {track.title} deleted"), 200
            else:
                return jsonify("Track not found"), 404
        
        
    return jsonify("Invalid request"), 400
    
    
if __name__ == '__main__':
    app.run(debug=True)