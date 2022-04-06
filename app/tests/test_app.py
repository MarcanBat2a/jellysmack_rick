from app import __version__
from fastapi.testclient import TestClient
from app import main

def test_version():
    assert __version__ == '0.1.0'

client = TestClient(main)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}