Feature: Tests pertaining to the GET /pet endpoint


  Scenario: Retrieve a pet with a valid ID
    Given I send a POST request to POST_PET_URL with body {"id": 10, "name": "test name"}
    And I save the value for id in the last response as pet_id
    When I send a get request to GET_PET_URL
    Then the request response should be 200