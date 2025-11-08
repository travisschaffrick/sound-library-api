import pytest
import os
from sqlalchemy import create_engine
from src.models import Base

# Set TESTING environment variable BEFORE importing app
os.environ['TESTING'] = '1'

# Now import app (it will use SQLite due to TESTING env var)
from src.app import app
import src.app as app_module

@pytest.fixture
def client():
    """Create test client with isolated test database"""
    # Create fresh test engine
    test_engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(test_engine)
    
    # Replace the global engine in app module
    original_engine = app_module.engine
    app_module.engine = test_engine
    
    app.config['TESTING'] = True
    
    with app.test_client() as test_client:
        yield test_client
    
    # Restore original engine and cleanup
    app_module.engine = original_engine
    Base.metadata.drop_all(test_engine)
    test_engine.dispose()