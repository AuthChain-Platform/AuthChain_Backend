from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the QR Scanner API for AuthChain"}

def test_scan_qr_image():
    with open("tests/test_qr_code.png", "rb") as f:
        response = client.post("/scan", files={"image": f})
        assert response.status_code == 200
        assert "result" in response.json()
        assert "type" in response.json()["result"]
        assert "data" in response.json()["result"]

# This is basically for Camera-based scanning
def test_scan_qr_camera():
    response = client.post("/scan")  
    assert response.status_code in [200, 400]
    assert "result" in response.json() or "error" in response.json()
