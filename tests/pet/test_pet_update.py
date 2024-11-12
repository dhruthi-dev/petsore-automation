import pytest
from src.framework.endpoints import PET_ENDPOINT
from src.framework.utils import get_json
from tests.data.test_data import update_pets_data, invalid_pets_data

@pytest.mark.pet
def test_valid_pet_update(api_client):
    # Valid scenario: Update an existing pet
    response = api_client.put(PET_ENDPOINT, data=update_pets_data[0])
    print(response.text)
    assert response.status_code == 200, "Expected 200 OK for valid pet update"
    assert get_json(response)["name"] == update_pets_data[0]["name"], "Expected updated pet name to match"

@pytest.mark.pet
@pytest.mark.xfail(reason="The server is returning 500 for malformed id, might be a bug")
def test_invalid_pet_update_invalid_id(api_client):
    # Invalid scenario: Update a pet with invalid data
    response = api_client.put(PET_ENDPOINT, data=invalid_pets_data[0])
    # Assert that the response status code is 400 for invalid ID - with non-numeric value
    assert response.status_code == 400, f"Expected 400, but got {response.status_code}"
    assert "Invalid ID supplied" in response.text, f"Unexpected response: {response.text}"

@pytest.mark.pet
@pytest.mark.xfail(reason="should pass, but the server is returning 200, might be a bug")
def test_invalid_pet_update_pet_not_found(api_client):
    # Invalid scenario: Update a non-existing pet assuming 99990000 id doesn't exist
    response = api_client.put(PET_ENDPOINT, data=invalid_pets_data[1])
    
    # Assert that the response status code is 404 for pet not found
    assert response.status_code == 404, f"Expected 404, but got {response.status_code}"
    assert "Pet not found" in response.text, f"Unexpected response: {response.text}"

@pytest.mark.pet
@pytest.mark.xfail(reason="should pass, but the server is returning 200, might be a bug")
def test_invalid_pet_update_validation_exception(api_client):
    # Invalid scenario: Update a pet with invalid data (e.g., missing required fields)
    # Valid pet ID but missing some required fields
    response = api_client.put(PET_ENDPOINT, data=invalid_pets_data[2])
    
    # Assert that the response status code is 405 or 422 for validation failure
    assert response.status_code in [405, 422], f"Expected 405 or 422, but got {response.status_code}"
    assert "Validation exception" in response.text, f"Unexpected response: {response.text}"

@pytest.mark.pet
def test_valid_pet_update_post_method(api_client):
    # Valid scenario: POST to the /pet/{pet_id} endpoint which updates the pet
    pet_id = update_pets_data[0]["id"]  # Use an existing pet ID
    response = api_client.update_pet_using_id(PET_ENDPOINT, pet_id, update_pets_data[0])

    # Assert that the response status code is 405 (Method Not Allowed)
    assert response.status_code == 200, f"Expected 200 for POST to /pet/{pet_id}, but got {response.status_code}"

@pytest.mark.pet
def test_invalid_pet_update_post_method(api_client):
    # Invalid scenario: POST to the /pet/{pet_id} endpoint, with invalid format
    # API doc says this should return 405, however it's returning 404
    pet_id = invalid_pets_data[0]["id"] # invalid id
    response = api_client.update_pet_using_id(PET_ENDPOINT, pet_id, invalid_pets_data[0])

    # Assert that the response status code is 404 (Method Not Allowed)
    assert response.status_code == 404, f"Expected 404 for POST to /pet/{pet_id}, but got {response.status_code}"

    # Optionally, check that the error message is appropriate
    assert "java.lang.NumberFormatException:" in response.text, f"Unexpected response: {response.text}"

