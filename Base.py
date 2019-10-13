import json
import requests

# This is Api key for the making the changes.
# Please update the API key before doing API calls
ApiKey = ""
ApiUrl = "https://api.github.com/gists/"
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(ApiKey)}


# This will create files in gist
def create_files_in_gist(id, update):
    update_create_helper_function(id, update)


# This will update files in user gist
def update_gist(id, update):
    update_create_helper_function(id, update)


# Helper method for creating and updating files
# in a gist for a user
def update_create_helper_function(id, update):
    api = ApiUrl + id
    response = requests.patch(api, json.dumps(update), headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        msg = "Error code " + str(response.status_code)
        msg = msg + "\nResponse " + str((response.json()))
        raise AssertionError(msg)


# This will retrieve gist of a user
def get_gist(id):
    api = ApiUrl + id
    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return response.status_code
    else:
        msg = "Error code " + str(response.status_code)
        msg = msg + "\nResponse " + str((response.json()))
        raise AssertionError(msg)



