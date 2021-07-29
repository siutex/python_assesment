import requests
from config import LOG


class Auth:

    def __init__(self):
        self.auth_url = "/token"

    def login(self, app_url, username, password):
        LOG.info("login")
        request_headers = {"Accept": "application/json",
                           "Authorization": "Basic ZWdnOmYwMEJhcmJBeiE="}
        payload = {"Username": username, "Password": password}
        LOG.debug(f"Request payload: {payload}")
        response = requests.post(
            f"{app_url}{self.auth_url}", headers=request_headers, data=payload)
        return response
