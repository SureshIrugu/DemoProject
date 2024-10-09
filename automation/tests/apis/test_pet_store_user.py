from http.client import responses

from playwright.sync_api import APIRequestContext,Playwright
from typing import Generator
import requests
import pytest

from automation.tests.config import api_key, base_uri,pet_id

file_path = "/automation/src/utils/pet.jpg"

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
)-> Generator[APIRequestContext,None,None]:
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


def test_add_pet(api_request_context: APIRequestContext) -> None:
    headers = {"Content-Type": "application/json", "x-api-key": api_key}  # Corrected to use a string
    data = {
            "id": 57576282,
            "category": {
                    "id": 11160318,
                    "name": "Dragon"
                     },
            "name": "doggie",
            "photoUrls": [
                "null data path"
                ],
            "tags": [
                {
                "id": 76998725,
                "name": "Thomas"
                }
            ],
             "status": "available"
    }

   # Make sure to use f-string correctly
    response = api_request_context.post(
        f"{base_uri}/pet", data = data, headers=headers
    )
    assert response.ok
    # Assert the response status
    assert response.status == 200
    # Assert the response name
    assert response.text().__contains__("Dragon")


def test_upload_image(api_request_context: APIRequestContext) -> None:
    # Set up the headers
    headers = {
        "x-api-key": api_key,
        "accept": "application/json"
    }
    # Prepare the file and metadata for the multipart request
    files = {
        "file": open("/Users/sureshirugu/Desktop/Swaglab/automationDemo/src/utils/pet.jpg", "rb")
    }
    data = {
        "additionalMetadata": "Nice"
    }

    # Make the API request
    response = requests.post(
        f"{base_uri}/pet/{pet_id}/uploadImage",
        files=files,
        data=data,
        headers=headers
    )

    # Assert the response status
    assert response.status_code == 200

def test_update_an_existing_pet(api_request_context: APIRequestContext) -> None:
    headers = {"Content-Type": "application/json", "x-api-key": api_key}
    data = {
            "id": pet_id,
            "category": {
                "id": 11160319,
                "name": "Nick"
            },
            "name": "doggie",
            "photoUrls": [
            "null data path"
            ],
            "tags": [{
                    "id": 76998725,
                    "name": "Thomas"
                    }],
            "status": "available"
    }
    response = api_request_context.put(
        f"{base_uri}/pet", data=data, headers=headers
    )
    # Assert the response status
    assert response.status == 200
    assert response.text().__contains__("Nick")

def test_find_pet_status(api_request_context: APIRequestContext) -> None:
    headers = {"Content-Type": "application/json", "x-api-key": api_key}  # Corrected to use a string
    payload = {
        "status": "available"
    }
   # Make sure to use f-string correctly
    response = api_request_context.get(
        f"{base_uri}/pet/findByStatus", params=payload, headers=headers
    )
    # Assert the response status
    assert response.status == 200

def test_find_pet_id(api_request_context: APIRequestContext) -> None:
    headers = {"Content-Type": "application/json", "x-api-key": api_key}  # Corrected to use a string

   # Make sure to use f-string correctly
    response = api_request_context.get(
        f"{base_uri}/pet/{pet_id}", headers=headers
    )
    # Assert the response status
    assert response.status == 200
    response_data = response.json()
    id = response_data.get("id")
    assert id == pet_id

def test_update_pet_in_the_store(api_request_context: APIRequestContext) -> None:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-api-key": api_key  # Content-Type will be set automatically by the `json` parameter
    }

    data = {
        "name": "petTest",
        "status": "deactivated"
    }
    response = api_request_context.post(
        f"{base_uri}/pet/{pet_id}", data=data, headers=headers
    )
    assert response.status == 200

def test_delete_a_pet(api_request_context: APIRequestContext) -> None:
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    response = api_request_context.delete(
        f"{base_uri}/pet/{pet_id}", headers=headers
    )
    assert response.status == 200










def test_get_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    get_todo = api_request_context.get(
        f"https://jsonplaceholder.typicode.com/posts/1",  headers=headers
    )
    assert get_todo.ok


def test_put_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    data = {
        "title": "foo2",
        "body": "bar",
        "userId": 1
    }
    put_todo = api_request_context.put(
        f"https://jsonplaceholder.typicode.com/posts/1", data=data, headers=headers
    )
    assert put_todo.ok
    assert put_todo.status == 200
    assert put_todo.json()["title"] == "foo2"


def test_delete_example(api_request_context: APIRequestContext):
    headers = {"Content-type": "application/json"}
    delete_todo = api_request_context.delete(
        f"https://jsonplaceholder.typicode.com/posts/1", headers=headers)
    assert delete_todo.ok
    assert delete_todo.status == 200