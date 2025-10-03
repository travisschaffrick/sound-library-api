from typing import List, Optional
from sqlalchemy import String, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    artist_name: Mapped[str] = mapped_column(String(200))
    duration_seconds: Mapped[int] = mapped_column(Integer)
    file_path: Mapped[str] = mapped_column(String(500))

    tags: Mapped[List["Tag"]] = relationship(secondary="track_tags", back_populates="tracks")


    def __repr__(self) -> str:
        return f"Tracks(id = {self.id!r}, title = {self.title}, artist_name = {self.artist_name}, duration_seconds = {self.duration_seconds}, file_path = {self.file_path})"

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    tracks: Mapped[List["Track"]] = relationship(secondary="track_tags", back_populates="tags")


    def __repr__(self) -> str:
        return f"Tags(id = {self.id!r}, name = {self.name})"

class track_tags(Base):
    __tablename__ = "track_tags"

    track_id: Mapped[int] = mapped_column(ForeignKey('tracks.id'))
    tag_id: Mapped[int] = mapped_column(ForeignKey('tags.id'))
    
    __table_args__ = (
            PrimaryKeyConstraint(track_id, tag_id),
        )
        