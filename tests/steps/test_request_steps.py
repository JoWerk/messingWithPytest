import logging
from src.request import send_request, update_request_url
from pytest_bdd import scenarios, step, parsers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

scenarios("../../features")


@step(parsers.parse("I send a {method} request to {url}"), target_fixture="request_result")
@step(parsers.parse("I send a {method} request to {url} with body {data}"), target_fixture="request_result")
def send_request_step(context, method, url, data=None):
    return send_request(update_request_url(context, url), method, data)


@step(parsers.parse("the request response should be {status:d}"))
def check_response_status(request_result, status):
    logging.info("The response status code from the previous request was " + str(request_result.status_code))

    assert request_result.status_code == status


@step(parsers.parse("I save the value for {response_key} in the last response as {context_key}"))
def save_value_from_response(context, request_result, response_key, context_key):
    context[context_key] = request_result.json()[response_key]