# Sound Library API

A REST API for managing audio files and their metadata. Supports creating, reading, updating, and deleting tracks, along with tagging and search functionality.

### Tech Stack
- Flask (Python web framework)
- PostgreSQL (relational database)
- SQLAlchemy (ORM)
- pytest (testing)

### Features (working)
- CRUD operations for audio tracks
- RESTful API design

### Features (planned)
- Tag management (many-to-many relationships)
- Search by title, artist, and tags
- Pagination for large datasets

### Prerequisites
- Python 3.x
- PostgreSQL installed locally
---
### Setup Instructions

1. **PostgreSQL**
    1. **Install PostgreSQL** (if not already installed)
        - macOS: `brew install postgresql`
        - Ubuntu/Debian: `sudo apt-get install postgresql`
        - Windows: Download from postgresql.org

    2. **Start PostgreSQL service**
        - macOS: `brew services start postgresql`
        - Linux: `sudo service postgresql start`
        - Windows: PostgreSQL should start automatically

    3. **Create the database**
        ```bash
        psql -U postgres
        CREATE DATABASE sound_library;
        \q
        ```
    4. **Set up authentication**
        1. Create a file named sqlalchemy_password.txt in the project root
        2. Add your PostgreSQL password on the first line
        3. Add this file to .gitignore (security!)

2. **Python Environment Setup**
    1. **Create virtual environment**
        ```bash
        python -m venv venv
        source venv/Scripts/activate
        ``` 
    2. **Install the dependencies**
        ```bash
        pip install -r requirements.txt
        ``` 
    3. **Run the application**
        ```
        python -m src.app
        ```
        The API will be available at http://localhost:5000

---
## API Documentation
### Base URL
`http://localhost:5000`

---

### Endpoints

#### 1. Create a track
**POST** `/api/tracks`

Creates a new track in the database.

**Request Body:**
```json
{
  "title": "Song Name",
  "artist_name": "Artist Name",
  "duration_seconds": 240,
  "file_path": "/path/to/file.mp3"
}
```
**Example:**
```bash
curl -X POST http://localhost:5000/api/tracks \
  -H "Content-Type: application/json" \
  -d '{"title":"Beware","artist_name":"Death Grips","duration_seconds":352,"file_path":"/music/beware.mp3"}'
```
**Response: `201 Created`**
```json
{
  "id": 1,
  "title": "Beware",
  "artist_name": "Death Grips",
  "duration_seconds": 352, 
  "file_path": "/music/beware.mp3"
}
```

#### 2. Edit a track
**PUT** `/api/tracks/:id`

Edits a track in the database.

**Example:**
```bash
curl -X PUT http://localhost:5000/api/tracks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Known for it", "file_path": "/music/knownforit.mp3", "duration_seconds": 253}'
```
**Response: `200 Success`**
```json
{
  "id": 1,
  "title": "Known for it",
  "artist_name": "Death Grips",
  "duration_seconds": 253, 
  "file_path": "/music/knownforit.mp3"
}
```
**Response: `404 Error`**
```json
{
  "Error": "Track not found"
}
```

#### 3. Delete a track
**DELETE** `/api/tracks/:id`

Delete a track in the database.

**Example:**
```bash
curl -X DELETE http://localhost:5000/api/tracks/1 \
  -H "Content-Type: application/json" \
```
**Response: `200 Success`**
```json
{
  "Success": "Track 1: Known for it deleted"
}
```
**Response: `404 Error`**
```json
{
  "Error": "Track not found"
}
```

#### 4. Get a track
**GET** `/api/tracks/:id`

Get a track from the database.

**Example:**
```bash
curl -X GET http://localhost:5000/api/tracks/1 \
  -H "Content-Type: application/json" \
```
**Response: `200 Success`**
```json
{
  "id": 1,
  "title": "Known for it",
  "artist_name": "Death Grips",
  "duration_seconds": 352, 
  "file_path": "/music/knownforit.mp3"
}
```
**Response: `404 Error`**
```json
{
  "Error": "Track not found"
}
```

#### 5. Get all tracks
**GET** `/api/tracks`

Get all tracks from the database.

**Example:**
```bash
curl -X GET http://localhost:5000/api/tracks \
  -H "Content-Type: application/json" \
```
**Response: `200 Success`**
```json
[
    {
        "id": 1,
        "title": "Known for it",
        "artist_name": "Death Grips",
        "duration_seconds": 352, 
        "file_path": "/music/knownforit.mp3"
    },
    {
        "id": 2,
        "title": "Get Got",
        "artist_name": "Death Grips",
        "duration_seconds": 191, 
        "file_path": "/music/getgot.mp3"
    }
]
```


_Project in progress - building this to learn production-level backend development._
