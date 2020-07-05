from fastapi.testclient import TestClient
from app.main import app
from app.api.author import authors
import logging
log = logging.getLogger('__name__')
import requests

client = TestClient(app)

def test_get_authors():
    response = client.get("/")
    assert response.status_code == 200

def test_get_author():
    response = client.get("/1")
    assert response.status_code == 200
