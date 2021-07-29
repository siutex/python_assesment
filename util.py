from config import LOG


def build_request_headers(access_token, accept_type="application/json",
                          **kwargs):
    LOG.info("build_request_headers")
    headers = {
        "X-API-KEY": f"{access_token}",
        "accept": accept_type
    }
    if "content_type" in kwargs:
        headers["Content-Type"] = kwargs["content_type"]

    LOG.debug(f"Request headers: {headers}")

    return headers
