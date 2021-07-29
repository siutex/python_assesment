from config import APP_URL, LOG, USER
import requests


def test_login_negative():
    # Login missing api key
    request_headers = {"Accept": "application/json",
                       "Authorization": "Basic ZWdnOmYwMEJhcmJBeiE="}
    payload = {"Username": "", "Password": ""}
    LOG.debug(f"Request payload: {payload}")
    response = requests.post(
        f"{APP_URL}/token", headers=request_headers, data=payload)
    response.status_code == 400
    response.text.__contains__("invalid username or password")
