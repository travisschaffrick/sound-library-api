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
        # Input validation
        if 'title' not in data or not data['title']:
            return jsonify({"Error": "No title"}), 400
        
        if 'artist_name' not in data or not data['artist_name']:
            return jsonify({"Error": "No artist name"}), 400
        
        if 'duration_seconds' not in data:
            return jsonify({"Error": "Duration is required"}), 400
        # Check type and value
        if not isinstance(data['duration_seconds'], int) or data['duration_seconds'] <= 0:
            return jsonify({"Error": "Duration must be a positive integer"}), 400

        if 'file_path' not in data or not data['file_path']:
            return jsonify({"Error": "No file path"}), 400
        
        song_tags = []

        with Session(engine) as session:
            if 'tags' in data:
                tag_names = data['tags']
                for tag_name in tag_names:
                    existing_tag = session.query(Tag).filter(Tag.name == tag_name).first()

                    if existing_tag:
                        song_tags.append(existing_tag)
                    else:
                        new_tag = Tag(name=tag_name)
                        song_tags.append(new_tag)

            track = Track(
                title = data['title'],
                artist_name = data['artist_name'],
                duration_seconds = data['duration_seconds'],
                file_path = data['file_path'],
                tags = song_tags
            )

            session.add(track)
            session.commit()
            session.refresh(track) # Adds id to python object (track.id)

            return jsonify({
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path,
                'tags': [tag.name for tag in track.tags]
            }), 201 #201 = Created
        

    elif request.method == 'GET':
        # Get pagination parameters from query string
        limit = request.args.get('limit', 20, type=int)  # default 20
        offset = request.args.get('offset', 0, type=int)  # default 0

        with Session(engine) as session:
            # Get count
            track_count = session.query(Track).count()


            # get paginated tracks
            statement = select(Track).limit(limit).offset(offset)
            result = session.execute(statement)
            tracks = result.scalars().all()
            
            # Convert to dictionaries
            tracks_list = [{
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path,
                'tags': [tag.name for tag in track.tags]
            } for track in tracks]

            # Return with pagination info
            return jsonify({
                'tracks': tracks_list,
                'total': total_count,
                'limit': limit,
                'offset': offset
            }), 200
    
    return jsonify("Invalid request"), 400
    
    
@app.route('/api/tracks/<id>', methods=['GET', 'PUT', 'DELETE'])
def handle_track_by_id(id):
    # GET
    if request.method == 'GET':        
        with Session(engine) as session:
            # get track
            statement = select(Track).where(Track.id == id)
            result = session.execute(statement)
            track = result.scalar_one_or_none()

            if not track:
                return jsonify({"Error": "Track not found"}), 404
            
            # Convert to dictionary
            tracks_list = {
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path,
                'tags': [tag.name for tag in track.tags]}
            return jsonify(tracks_list), 200
        
    # PUT
    if request.method == 'PUT':
        data = request.get_json()

        with Session(engine) as session:
            # get track
            statement = select(Track).where(Track.id == id)
            result = session.execute(statement)
            track = result.scalar_one_or_none()

            if not track:
                return jsonify({"Error": "Track not found"}), 404
            
            # update only what is given
            if 'title' in data and data['title']:
                track.title = data['title']
            if 'artist_name' in data and data['artist_name']:
                track.artist_name = data['artist_name']
            if 'duration_seconds' in data and isinstance(data['duration_seconds'], int) \
                and data['duration_seconds'] > 0:
                track.duration_seconds = data['duration_seconds']
            if 'file_path' in data and data['file_path']:
                track.file_path = data['file_path']

            if 'tags' in data:
                song_tags = []
                tag_names = data['tags']
                for tag_name in tag_names:
                    existing_tag = session.query(Tag).filter(Tag.name == tag_name).first()

                    if existing_tag:
                        song_tags.append(existing_tag)
                    else:
                        new_tag = Tag(name=tag_name)
                        song_tags.append(new_tag)
                track.tags = song_tags

            session.commit()
            session.refresh(track)
            
            return jsonify({
                'id': track.id,
                'title': track.title,
                'artist_name': track.artist_name,
                'duration_seconds': track.duration_seconds,
                'file_path': track.file_path,
                'tags': [tag.name for tag in track.tags]
            }), 200
    
    # DELETE
    if request.method == 'DELETE':
        with Session(engine) as session:
            # get track
            statement = select(Track).where(Track.id == id)
            result = session.execute(statement)
            track = result.scalar_one_or_none()
            if track:
                session.delete(track)
                session.commit()
                return jsonify({"Success": f"Track {id}: {track.title} deleted"}), 200
            else:
                return jsonify({"Error": "Track not found"}), 404
        
        
    return jsonify("Invalid request"), 400

@app.route('/api/tracks/search', methods=['GET'])
def search_tracks():
    query = request.args.get('q', '')

    if not query:
        return jsonify({"Error": "Search query required"}), 400

    # Get pagination parameters
    limit = request.args.get('limit', 20, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    
    with Session(engine) as session:
        search_pattern = f'%{query}%'

        # Search using track title, artist name, and track tags
        base_statement = select(Track).join(Track.tags).where(
            (Track.title.ilike(search_pattern)) |
            (Track.artist_name.ilike(search_pattern)) |
            (Tag.name.ilike(search_pattern))
        ).distinct()

        # Get total count
        total_count = len(session.execute(base_statement).scalars().all())

        # Pagination
        statement = base_statement.limit(limit).offset(offset)
        result = session.execute(statement)
        tracks = result.scalars().all()

        # Convert to dictionaries
        tracks_list = [{
            'id': track.id,
            'title': track.title,
            'artist_name': track.artist_name,
            'duration_seconds': track.duration_seconds,
            'file_path': track.file_path,
            'tags': [tag.name for tag in track.tags]
        } for track in tracks]

        # Return with pagination info
        return jsonify({
            'tracks': tracks_list,
            'total': total_count,
            'limit': limit,
            'offset': offset,
            'query': query
        }), 200
    
if __name__ == '__main__':
    app.run(debug=True)