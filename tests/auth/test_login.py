from libs.auth import Auth
from config import APP_URL, LOG, USER, PASSWORD


def test_login():
    LOG.info("test_login")
    response = Auth().login(APP_URL, USER, PASSWORD)
    LOG.debug(response.json())
    assert response.ok
    assert response.status_code == 200
