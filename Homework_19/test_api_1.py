from utils import load_schema, URL, user
import jsonschema
import requests

url = 'https://reqres.in'


def test_get_single_resource_successfully():
    schema = load_schema("get_single_resource.json")
    result = requests.get(url + URL.single_resource)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_get_users_list_successfully():
    schema = load_schema("get_users_list.json")
    result = requests.get(url + URL.users_list)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_user_not_found():
    result = requests.get(url + URL.incorrect_user)

    assert result.status_code == 404
    jsonschema.validate(result.json(), {})


def test_create_user():
    schema = load_schema("post_create_user.json")
    result = requests.post(url=url + URL.users_url, json=user("morpheus", "leader"))

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)
    assert result.json()["name"] == "morpheus"

    global morpheus_id
    morpheus_id = result.json()["id"]


def test_update_user_morpheus():
    schema = load_schema("put_update_user.json")
    result = requests.put(url=url + URL.users_url + '/' + morpheus_id, json=user("morpheus", "zion resident"))

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)
    assert result.json()["job"] == "zion resident"


def test_delete_user_morpheus():
    result = requests.delete(url=url + URL.users_url + '/' + morpheus_id)

    assert result.status_code == 204
    assert result.text == ''


def test_unsuccessful_login():
    result = requests.post(url=url + URL.login_url, json={"email": "email"})

    assert result.status_code == 400
    assert result.json()["error"] == "Missing password"
