from starlette.testclient import TestClient
from app.main import app
from app.api.book import books
import logging
log = logging.getLogger('__name__')

client = TestClient(app)

def test_get_books():
    response = client.get("/")
    assert response.status_code == 200
