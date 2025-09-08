from wsgiref import headers
import requests

base_url = 'https://yougile.com/'
token = "e03BzyeqiIikD3hez7-PD5ML2XFS2OP+szvq6YaGlV6VzeXK0vnH4OZi8eNOfs6h"
HEADERS = {"Authorization": f"Bearer {token}"}
id_project = "0e9780be-2f90-42b1-840a-b7f8b9143eb2"

def test_create_project_positive():
    resp = requests.post(base_url+'api-v2/projects', json={"title": "Test"}, headers=HEADERS)
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    print("Создан проект:", project_id)
    assert "id" in resp.json()

def test_create_project_negative():
    resp = requests.post(base_url+'api-v2/projects', json={"title": ""}, headers=HEADERS)
    assert resp.status_code == 400
    
def test_change_project_positive():
    resp = requests.put(f"{base_url}api-v2/projects/{id_project}", json={"title": "Test2"}, headers=HEADERS)
    assert resp.status_code == 200
    response_data = resp.json()
    changed_project_id = response_data["id"]
    assert changed_project_id

def test_change_project_negative():
    resp = requests.put(f"{base_url}api-v2/projects/{id_project}", json={"title": ""}, headers=HEADERS)
    assert resp.status_code == 400

def test_get_project_positive():
    resp = requests.get(f"{base_url}api-v2/projects/{id_project}", headers=HEADERS)
    assert resp.status_code == 200
    response_data = resp.json()
    get_project_id = response_data["id"]
    assert get_project_id

def test_get_project_negative():
    resp = requests.get(f"{base_url}api-v2/projects/123", headers=HEADERS)
    assert resp.status_code == 404