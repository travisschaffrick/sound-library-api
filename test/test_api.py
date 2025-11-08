import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.app import app
from src.models import Base, Track


def test_create_track(client):
    """Test POST /api/tracks - Create a new track"""
    response = client.post('/api/tracks', json={
        'title': 'Beware',
        'artist_name': 'Death Grips',
        'duration_seconds': 352,
        'file_path': '/music/beware.mp3'
    })
    
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Beware'
    assert data['artist_name'] == 'Death Grips'
    assert data['duration_seconds'] == 352
    assert 'id' in data


def test_create_track_missing_title(client):
    """Test POST /api/tracks - Missing title returns 400"""
    response = client.post('/api/tracks', json={
        'artist_name': 'Death Grips',
        'duration_seconds': 352,
        'file_path': '/music/beware.mp3'
    })
    
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_create_track_invalid_duration(client):
    """Test POST /api/tracks - Invalid duration returns 400"""
    response = client.post('/api/tracks', json={
        'title': 'Beware',
        'artist_name': 'Death Grips',
        'duration_seconds': -10,  # Invalid: negative
        'file_path': '/music/beware.mp3'
    })
    
    assert response.status_code == 400


def test_get_all_tracks(client):
    """Test GET /api/tracks - List all tracks"""
    # First create some tracks
    client.post('/api/tracks', json={
        'title': 'Hot Head',
        'artist_name': 'Death Grips',
        'duration_seconds': 200,
        'file_path': '/music/hothead.mp3'
    })
    client.post('/api/tracks', json={
        'title': 'Beware',
        'artist_name': 'Death Grips',
        'duration_seconds': 352,
        'file_path': '/music/beware.mp3'
    })
    
    # Get all tracks
    response = client.get('/api/tracks')
    
    assert response.status_code == 200
    data = response.get_json()
    
    assert data['total'] == 2
    assert len(data['tracks']) == 2
    assert data['limit'] == 20
    assert data['offset'] == 0


def test_get_track_by_id(client):
    """Test GET /api/tracks/<id> - Get single track"""
    # Create a track
    create_response = client.post('/api/tracks', json={
        'title': 'Beware',
        'artist_name': 'Death Grips',
        'duration_seconds': 352,
        'file_path': '/music/beware.mp3'
    })
    track_id = create_response.get_json()['id']
    
    # Get the track
    response = client.get(f'/api/tracks/{track_id}')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Beware'
    assert data['id'] == track_id


def test_get_nonexistent_track(client):
    """Test GET /api/tracks/<id> - Nonexistent track returns 404"""
    response = client.get('/api/tracks/9999')
    
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data


def test_update_track(client):
    """Test PUT /api/tracks/<id> - Update track"""
    # Create a track
    create_response = client.post('/api/tracks', json={
        'title': 'Hot Head',
        'artist_name': 'Death Grips',
        'duration_seconds': 200,
        'file_path': '/music/hothead.mp3'
    })
    track_id = create_response.get_json()['id']
    
    # Update the track
    response = client.put(f'/api/tracks/{track_id}', json={
        'title': 'Hot Head (Updated)',
        'duration_seconds': 205
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Hot Head (Updated)'
    assert data['duration_seconds'] == 205
    assert data['artist_name'] == 'Death Grips'  # Unchanged


def test_delete_track(client):
    """Test DELETE /api/tracks/<id> - Delete track"""
    # Create a track
    create_response = client.post('/api/tracks', json={
        'title': 'Beware',
        'artist_name': 'Death Grips',
        'duration_seconds': 352,
        'file_path': '/music/beware.mp3'
    })
    track_id = create_response.get_json()['id']
    
    # Delete the track
    response = client.delete(f'/api/tracks/{track_id}')
    
    assert response.status_code == 200
    
    # Verify it's gone
    get_response = client.get(f'/api/tracks/{track_id}')
    assert get_response.status_code == 404


def test_delete_nonexistent_track(client):
    """Test DELETE /api/tracks/<id> - Deleting nonexistent track returns 404"""
    response = client.delete('/api/tracks/9999')
    
    assert response.status_code == 404