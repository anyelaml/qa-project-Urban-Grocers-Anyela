import configuration
import data
import requests

def post_new_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers)

    response = post_new_user()
    if response.status_code == 201:
        auth_token = response.json().get('authToken')
        print(f'authToken generado:{auth_token}')
    else:
        print(f"error al crear usuario:{response_user.json()}")


def post_new_client_kit(kit_body):
    auth_token = post_new_user()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)
    return response

