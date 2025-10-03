from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.models import Base, Track, Tag, track_tags

# Get password
with open("sqlalchemy_password.txt") as f:
    password = f.readline().strip()

# Create Database and tables
engine = create_engine(f"postgresql://postgres:{password}@localhost/sound_library")
Base.metadata.create_all(engine)

with Session(engine) as session:
    track = Track(
        title = "Spread Eagle Across The Block",
        artist_name = "Death Grips",
        duration_seconds = 232,
        file_path = "/music/deathgrips/spreadeagleacrosstheblock.mp3"
    )
    session.add(track)
    session.commit()
    print(f"Created: {track}")