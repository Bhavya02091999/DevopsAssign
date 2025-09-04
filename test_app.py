import pytest
from ACEest_Fitness import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Welcome to ACEest Fitness & Gym!"

def test_plans(client):
    response = client.get('/plans')
    assert response.status_code == 200
    data = response.get_json()
    assert "plans" in data
    assert len(data["plans"]) == 3
    assert all("name" in p and "price" in p for p in data["plans"])

def test_trainers(client):
    response = client.get('/trainers')
    assert response.status_code == 200
    data = response.get_json()
    assert "trainers" in data
    assert isinstance(data["trainers"], list)
