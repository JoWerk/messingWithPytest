from src import request
base_url = "https://petstore3.swagger.io/"
base_path = "/api/v3"
post_path = "/pet"


# TODO: Add in the bdd layer here as well.  Then we can see how gpt reacts to this

def test_post_pet_only_required():
    data = {
      "id": 10,
      "name": "doggie"
    }
    url = base_url + base_path + post_path
    request.post(url, data)
