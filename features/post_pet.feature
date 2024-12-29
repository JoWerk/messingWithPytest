Feature: Tests pertaining to the POST /pet endpoint
  # TODO: Ask gpt to write more tests

  Scenario: Successful request with valid required fields only
    When I send a POST request to POST_PET_URL with body {"id": 10, "name": "test name"}
    Then the request response should be 200

  Scenario: Unsuccessful request with invalid id
    When I send a POST request to POST_PET_URL with body {"id": "invalid_id", "name": "test name"}
    Then the request response should be 400

