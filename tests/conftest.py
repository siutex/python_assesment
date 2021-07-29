import pytest
import requests
from config import SESSION, APP_URL, USER, PASSWORD, LOG
from libs.auth import Auth


@pytest.fixture(scope="session")
def login_as_user():
    LOG.info("login_as_user")
    response = Auth().login(APP_URL, USER, PASSWORD)
    assert response.ok

    access_token = response.json()["key"]
    yield access_token
