from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'akmaliktest'
    assert response.json()['email'] == 'akmaliktest@email.com'
    assert response.json()['first_name'] == 'Amit'
    assert response.json()['last_name'] == 'Test'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '1234567890'