import pytest
from app import app as flak_app

@pytest.fixture
def client (app):
    return app.test_client()
