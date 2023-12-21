# from ..main import app
from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)




def test_root():
    """Return a simple hello world repsonse"""

    response = client.get("/")
    
    print(response.status_code)
    json_response = response.json()
    print(json_response)
    assert response.status_code == 200
    assert json_response == {"Hello":"World"}