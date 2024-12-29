import json
import logging
from copy import deepcopy

import requests

from src import urls


def send_request(url, method, data=None):
    if method.lower() == "post":
        response = requests.post(url, json=json.loads(data))
    elif method.lower() == "get":
        response = requests.get(url)
    elif method.lower() == "put":
        response = requests.put(url, json=json.loads(data))
    elif method.lower() == "delete":
        response = requests.delete(url)
    else:
        raise Exception("Invalid method")

    if data is not None:
        logging.info("A " + method.upper() + " request to " + url + "with body " + str(data) + " was sent successfully.")
    else:
        logging.info("A " + method.upper() + " request to " + url + " was sent successfully.")
    logging.info("The response for the " + method.upper() + " request contained the body " + str(response.json()))

    return response


def update_request_url(context, url):
    try:
        url = getattr(urls, url)
        if "{" in url and "}" in url:
            tmp = deepcopy(url)
            while "{" in tmp:
                tmp = url.split("{")[1]
                tmp = tmp.split("}")
                path_var = tmp[0]
                tmp = tmp[1]

                url = url.replace("{" + path_var + "}", str(context[path_var]))

    except AttributeError:
        url = urls.BASE_URL + url


    return url