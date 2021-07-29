from Client.clients import Clients
from config import APP_URL, LOG


def test_client_crud(login_as_user):
    LOG.info("test_client_CRUD")

    # Create new client
    first_name = "test29"
    last_name = "solo"
    phone = "+48 800 190 591"
    response = Clients().create_client(APP_URL, login_as_user, first_name,
                                       last_name, phone)
    assert response.ok

    response_data = response.json()
    new_client_id = response_data["id"]
    assert response_data["firstName"] == first_name
    assert response_data["lastName"] == last_name
    assert response_data["phone"] == phone

    # Check the new client can get his  info
    response = Clients().get_client_by_id(APP_URL, login_as_user, new_client_id)
    assert response.ok
    assert response.json()["firstName"] == first_name
    assert response.json()["lastName"] == last_name

    # Update Client data
    last_name_update = "duo"
    response = Clients().update_client(APP_URL, login_as_user, first_name,
                                       last_name_update, phone, new_client_id)
    assert response.ok

    response_data = response.json()
    new_client_id = response_data["id"]
    assert response_data["firstName"] == first_name
    assert response_data["lastName"] == last_name_update
    assert response_data["phone"] == phone

    # Get all clients
    response = Clients().get_all_clients(APP_URL, login_as_user)
    assert response.ok
    assert len(response.content) > 0

    # Finally, delete the newly created client
    response = Clients().delete_client(APP_URL, login_as_user, new_client_id)
    assert response.ok
