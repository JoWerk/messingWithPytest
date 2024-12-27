Feature: Tests pertaining to the POST /pet endpoint
  # TODO: set up urls in global way (add a baseurl, use getattr to get path, etc)
  # TODO: Ask gpt to write more tests

  Scenario: Successful request with valid required fields only
    When I send a post request to https://petstore3.swagger.io/api/v3/pet with body {"id": 10,"name": "test name"}
    Then the request response should be 200

  Scenario: Unsuccessful request with invalid id
    When I send a post request to https://petstore3.swagger.io/api/v3/pet with body {"id": "invalid_id","name": "test name"}
    Then the request response should be 400