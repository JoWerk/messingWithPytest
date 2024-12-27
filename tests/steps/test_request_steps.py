import json

import requests
import logging

from pytest_bdd import scenarios, step, when, parsers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scenarios("../../features")

@step(parsers.parse("I send a {method} request to {url}"), target_fixture="request_result")
@step(parsers.parse("I send a {method} request to {url} with body {data}"), target_fixture="request_result")
def send(method, url, data=None):
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

    logging.info("Sent request: " + str(data))
    logging.info("Response: " + str(response.content))

    return response


@step(parsers.parse("the request response should be {status:d}"))
def check_response_status(request_result, status):
    logging.info("Response status: " + str(request_result.status_code))

    assert request_result.status_code == status