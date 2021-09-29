from fastapi.testclient import TestClient
from index import *

client = TestClient(app)

def test_get_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Home Microservice"}

def test_get_properties_by_id():
    response = client.get("/properties/0")
    assert response.status_code == 404
    assert response.json() == {"detail": "Property Info Not Found"}

def test_get_properties_by_id_exists():
    response = client.get("/properties/1")
    assert response.status_code == 200

def test_get_properties():
    response = client.get("/")
    assert response.status_code == 200
    assert len(response.json()) > 0