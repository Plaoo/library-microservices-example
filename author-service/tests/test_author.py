from starlette.testclient import TestClient
from app.main import app
from app.api.author import authors

client = TestClient(app)


def test_create_author():
    dummy_data = {
        "firstname": "Stephen",
        "surname": "King",
        "year_of_birth": 1947,
        "nationality": "USA",
    }

    response = client.post("http://172.30.0.1/api/v1/authors", json=dummy_data)
    assert response.status_code == 200


#def test_get_authors():
#    response = client.get("http://localhost/api/v1/authors")
#    assert response.status_code == 200


# def test_get_author():
#    response = requests.get("http://0.0.0.0:8000/api/v1/authors/1")
#    assert response.status_code == 200
