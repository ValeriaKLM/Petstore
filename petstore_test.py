import pytest
import configuration
import requests
from data import pet_body, user_body, order_body, login_user_body, headers, pet_image_body, users_bodies

created_pet_id = None

def test_create_pet():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_PET_PATH,
                             json=pet_body,
                             headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == pet_body['name']


def test_upload_image_of_pet():
    pet_id = pet_body['id']
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_PET_PATH + f'/{{petId}}/uploadImage'.format(petId=pet_id),
                             files=pet_image_body)
    assert response.status_code == 200
    assert 'File uploaded to' in response.json()['message']


def test_update_pet():
    updated_pet = pet_body.copy()
    updated_pet['name'] = 'updated name'
    response = requests.put(configuration.URL_SERVICE + configuration.CREATE_PET_PATH,
                            json=updated_pet,
                            headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == updated_pet['name']


def test_find_pet_by_status():
    pet_status = "available"
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_PET_PATH + f'/findByStatus',
                            params={"status": pet_status})
    assert response.status_code == 200
    pets_list = response.json()
    assert isinstance(pets_list, list)
    for pet in pets_list:
        assert pet['status'] == pet_status


def test_find_pet_by_id():
    new_pet = requests.post(configuration.URL_SERVICE + configuration.CREATE_PET_PATH,
                            json=pet_body,
                            headers=headers)
    pet_id = new_pet.json()['id']
    assert pet_id is not None, "Нет доступных питомцев"
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_PET_PATH + f'/{{petId}}'.format(petId=pet_id))
    assert response.status_code == 200
    assert response.json()['id'] == pet_id


def test_update_pet_with_form_data():
    updated_pet = pet_body.copy()
    updated_pet['name'] = 'DoggieCutie'
    response = requests.put(configuration.URL_SERVICE + configuration.CREATE_PET_PATH,
                            json=updated_pet)
    assert response.status_code == 200
    assert response.json()['name'] == updated_pet['name']


def test_delete_a_pet():
    new_pet = requests.post(configuration.URL_SERVICE + configuration.CREATE_PET_PATH,
                            json=pet_body,
                            headers=headers)
    pet_id = new_pet.json()['id']
    response = requests.delete(configuration.URL_SERVICE + configuration.CREATE_PET_PATH + f'/{{petId}}'.format(petId=pet_id))
    assert response.status_code == 200


def test_create_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f'/order',
                             json=order_body,
                             headers=headers)
    assert response.status_code == 200
    assert response.json()['status'] == order_body['status']


def test_return_pet_inventories_by_status():
    order_status = "available"
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f'/inventory',
                            params={"status": order_status},
                            headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert order_status in response.json()


def test_find_purchase_order_by_id():
    new_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f'/order',
                              json=order_body,
                              headers=headers)
    order_id = new_order.json()['id']
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f'/order/{{orderId}}'.format(orderId=order_id))
    assert response.status_code == 200
    assert response.json()['id'] == order_id


def test_delete_purchase_order_by_id():
    new_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f'/order',
                              json=order_body,
                              headers=headers)
    order_id = new_order.json()['id']
    response = requests.delete(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f'/order/{{orderId}}'.format(orderId=order_id))
    assert response.status_code == 200


def test_create_list_of_users():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH + f'/createWithList',
                             json=users_bodies,
                             headers=headers)
    assert response.status_code == 200
    assert response.json()['message'] == 'ok'


def test_create_user():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=user_body,
                             headers=headers)
    assert response.status_code == 200


def test_get_user_by_username():
    username = user_body['username']
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH + f'/{{username}}'.format(username=username),
                            headers=headers)
    assert response.status_code == 200
    assert response.json()['username'] == username


def test_log_user_into_system():
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH + f'/login',
                            params=login_user_body,
                            headers=headers)
    assert response.status_code == 200
    assert 'logged in user session:' in response.json()['message']


def test_log_current_user_out_of_system():
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_USER_PATH + f'/logout',
                            headers=headers)
    assert response.status_code == 200
    assert response.json()['message'] == 'ok'


def test_update_user():
    updated_user = user_body.copy()
    updated_user['username'] = 'updatedUsername'
    response = requests.put(configuration.URL_SERVICE + configuration.CREATE_USER_PATH + f'/{{username}}',
                            json=updated_user,
                            headers=headers)
    assert response.status_code == 200


def test_delete_user():
    username = user_body['username']
    response = requests.delete(configuration.URL_SERVICE + configuration.CREATE_USER_PATH + f'/{{username}}'.format(username=username))
    assert response.status_code == 200
