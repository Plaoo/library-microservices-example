from starlette.testclient import TestClient
from app.main import app
from app.api.author import authors
import logging
log = logging.getLogger('__name__')
import requests

def test_get_authors():
    response = requests.get('http://0.0.0.0:8080/api/v1/authors')
    assert response.status_code == 200
#client = TestClient(app)
#
#def test_get_authors():
#    response = client.get("/")
#    assert response.status_code == 200
#
#def test_get_author():
#    response = client.get("/1")
#    assert response.status_code == 200
