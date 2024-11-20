from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the QR Scanner API"}

def test_scan_qr():
    mock_data = {"image": "test_image_data"}
    response = client.post("/scan", json=mock_data)
    assert response.status_code == 200
    assert "result" in response.json()
