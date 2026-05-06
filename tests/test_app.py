from fastapi.testclient import TestClient 
from app.main import app 

client = TestClient(app) 

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200 
    assert "Enter Feature Value" in response.text 

def test_prediction():
    response = client.post("/predict", data={"feature": 5})
    assert response.status_code == 200 
    assert "Prediction" in response.text 

def test_model_logic():
    from app.model import predict 
    assert predict(5) == 15 