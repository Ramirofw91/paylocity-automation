import pytest
import requests

#1 Authentication and login
def test_authentication(auth_session):
    url_api = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/Benefits"
    response = auth_session.get(url_api)
    assert response.status_code == 200
    print("Respuesta API:", response.text)

#2 Get Employee list
def test_getEmployeeList(auth_session):
    url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees"
    response = auth_session.get(url)
    assert response.status_code == 200
    data = response.json()
    print("Lista de empleados:", data)
    assert isinstance(data, list)
    #print (list)

#3 Post New Employe
def test_postEmployee(auth_session):
    url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees"
    payload = {
        "firstName": "test2",
        "lastName": "test3",
        "dependants": 2
    }
    response = auth_session.post(url, json=payload)
    assert response.status_code in [200, 201]
    print("API response:", response.json())
    data = response.json()
    assert data["firstName"] == "test2"
    assert data["lastName"] == "test3"
    assert data["dependants"] == 2

#4 Update Employee
def test_update_employee(auth_session):
    url = "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees"
    payload = {
        "id": "01e3e97e-d828-4434-9dde-93071dc21dbd",
        "firstName": "updatetest",
        "lastName": "lastnameupdate",
        "dependants": 2,
        "username": "user_test"
    }

    response = auth_session.put(url, json=payload)
    assert response.status_code in [200, 204]
    print("Respuesta:", response.json() if response.content else "No content")

#5 Delete Employee
def test_delete_Employee(auth_session):
    employee_id = "01e3e97e-d828-4434-9dde-93071dc21dbd"
    url = f"https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod/api/employees/{employee_id}"

    response = auth_session.delete(url)
    assert response.status_code == 200 or response.status_code == 204
    print("Respuesta al eliminar:", response.status_code)

