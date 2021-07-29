import requests
from util import build_request_headers
from config import SESSION, LOG


class Clients:

    def __init__(self):
        self.clients_url = "/clients"
        self.client_url = "/client"

    def get_all_clients(self, app_url, access_token):
        LOG.info("get_all_users")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(
            f"{app_url}{self.clients_url}", headers=request_headers)
        return response

    def create_client(self, app_url, access_token, first_name, last_name, phone):
        LOG.info("create_client")
        request_headers = build_request_headers(access_token,
                                                content_type="application/json")
        payload = {"firstName": first_name, "lastName": last_name,
                   "phone": phone}
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.post(f"{app_url}{self.client_url}",
                                headers=request_headers, json=payload)
        return response

    def update_client(self, app_url, access_token, first_name, last_name, phone, client_id):
        LOG.info("update_client")
        request_headers = build_request_headers(access_token,
                                                content_type="application/json")
        payload = {"firstName": first_name, "lastName": last_name,
                   "phone": phone}
        LOG.debug(f"Request payload: {payload}")
        response = SESSION.put(f"{app_url}{self.client_url}/{client_id}",
                               headers=request_headers, json=payload)
        return response

    def get_client_by_id(self, app_url, access_token, client_id):
        LOG.info("get_client_user")
        request_headers = build_request_headers(access_token)
        response = SESSION.get(
            f"{app_url}{self.client_url}/{client_id}", headers=request_headers)
        return response

    def delete_client(self, app_url, access_token, client_id):
        LOG.info("delete_client")
        request_headers = build_request_headers(access_token)
        response = SESSION.delete(f"{app_url}{self.client_url}/{client_id}",
                                  headers=request_headers)
        return response
