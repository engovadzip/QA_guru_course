import json
import os


def load_schema(filepath):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/schemas/' + filepath) as file:
        schema = json.load(file)
        return schema


def user(name, job):
    info = {
        "name": f"{name}",
        "job": f"{job}"
    }

    return info


class URL:
    single_resource = '/api/unknown/3'

    users_list = '/api/users?page=1'

    incorrect_user = '/api/users/23'

    users_url = '/api/users'

    login_url = '/api/login'

