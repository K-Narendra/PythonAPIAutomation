import requests
import string
import json
import random

base_url = "https://reqres.in"

def get_users():
    url = base_url + "/api/users?page=2"
    header = {"Accept":"*/*"}
    print("Getting User from API === >")
    response = requests.get(url,headers=header)
    assert response.status_code == 200
    raw_data = response.json()
    json_data = json.dumps(raw_data, indent=3)
    print(json_data)


def create_user():
    url = base_url+"/api/users"
    data ={
        "name" : "Narendra",
        "job": "SDET"
    }
    response = requests.post(url, json=data)

    print(response)
    assert response.status_code == 201
    raw_data = response.json()
    json_data = json.dumps(raw_data,indent=4)
    print(json_data)
    return raw_data["id"]


def update_user(id):
    url = base_url + f"/api/users/2{id}"
    data = {
        "name": "Narendra kanakdande",
        "job": "SDET2"
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200
    raw_data = response.json()
    assert raw_data["name"] == "Narendra kanakdande"
    json_data = json.dumps(raw_data, indent=4)
    print("Updated Data ====>\n",json_data)


def delete_user(id):
    url = base_url+f"/api/users/2{id}"
    response = requests.delete(url)
    assert response.status_code == 204
    print("User deleted sucessfully")


def get_toke():
    url = base_url + f"/api/register"
    body = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
         }
    response = requests.post(url,json=body)
    assert response.status_code == 200
    token = response.json().get("token")
    print(token)




# get_users()
# id =create_user()
# update_user(id)
# delete_user(id)'

get_toke()