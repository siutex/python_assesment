from Client.clients import Clients
from config import APP_URL, LOG


def test_client_invalid_body(login_as_user):
    # Create new client missing data
    last_name = "solo"
    phone = "+48 800 190 591"
    response = Clients().create_client(APP_URL, login_as_user, "",
                                       last_name, phone)
    assert response.status_code == 400
    assert response.text.__contains__("required")

    # Update  client missing data
    first_name = "test29"
    last_name = "solo"
    phone = "+48 800 190 591"
    response = Clients().create_client(APP_URL, login_as_user, first_name,
                                       last_name, phone)
    assert response.ok
    response_data = response.json()
    new_client_id = response_data["id"]

    response2 = Clients().update_client(APP_URL, login_as_user, first_name,
                                        '', phone, new_client_id)

    assert response2.status_code == 400
    assert response2.text.__contains__("required")


def test_client_invalid_api_key(login_as_user):
    # Create new client missing key
    first_name = "test29"
    last_name = "solo"
    phone = "+48 800 190 591"
    response = Clients().create_client(APP_URL, '', first_name,
                                       last_name, phone)
    assert response.status_code == 403
    assert response.text.__contains__("invalid or missing api key")

    response = Clients().get_all_clients(APP_URL, '')
    assert response.status_code == 403
    assert response.text.__contains__("invalid or missing api key")

    # Update  client missing key
    first_name = "test29"
    last_name = "solo"
    phone = "+48 800 190 591"
    response = Clients().create_client(APP_URL, login_as_user, first_name,
                                       last_name, phone)
    assert response.ok
    response_data = response.json()
    new_client_id = response_data["id"]

    response = Clients().update_client(APP_URL, '', first_name,
                                       '', phone, new_client_id)

    assert response.status_code == 403
    assert response.text.__contains__("invalid or missing api key")

    # Update  client missing key
    first_name = "test29"
    last_name = "solo"
    phone = "+48 800 190 591"
    response = Clients().create_client(APP_URL, login_as_user, first_name,
                                       last_name, phone)
    assert response.ok
    response_data = response.json()
    new_client_id = response_data["id"]

    response = Clients().update_client(APP_URL, '', first_name,
                                       '', phone, new_client_id)

    assert response.status_code == 403
    assert response.text.__contains__("invalid or missing api key")

    # Delete client missing key
    response = Clients().delete_client(APP_URL, '', new_client_id)
    assert response.status_code == 403
    assert response.text.__contains__("invalid or missing api key")

    # Get clients missing key
    response = Clients().get_all_clients(APP_URL, '')
    assert response.status_code == 403
    assert response.text.__contains__("invalid or missing api key")


def test_client_not_fount(login_as_user):
    # Delete client not found
    response = Clients().delete_client(APP_URL, login_as_user, '9999999')
    assert response.status_code == 404
    assert response.text.__contains__("client not found")
