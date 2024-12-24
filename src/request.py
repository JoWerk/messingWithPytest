import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def post(url, data):
    response = requests.post(url, json=data)
    logging.info("Sent request: " + str(data))

    # Check if the pet was created successfully
    if response.status_code == 200:
        logging.info("POST request successful: " + str(response.content))
        # Return the pet ID of the created pet
        return response.json()
    else:
        logging.error(f"POST request failed: " + str(response.content))
        assert False
