from flask import Flask, jsonify, request
from src.models import Base, Track, Tag, track_tags
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Get password
with open("sqlalchemy_password.txt") as f:
    password = f.readline().strip()

# Create Database and tables
engine = create_engine(f"postgresql://postgres:{password}@localhost/sound_library")
Base.metadata.create_all(engine)


app = Flask(__name__)

@app.route('/api/tracks', methods=['POST'])
def add_track():
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
    
if __name__ == '__main__':
    app.run(debug=True)