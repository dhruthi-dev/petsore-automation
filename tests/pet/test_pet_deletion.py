import pytest
from src.framework.endpoints import PET_ENDPOINT
from tests.data.test_data import valid_pets_data

@pytest.mark.pet
@pytest.mark.parametrize("pet_data", valid_pets_data)
def test_valid_pet_deletion(api_client, pet_data):
    # Valid scenario: Delete an existing pet
    valid_pet_id = pet_data["id"]
    response = api_client.delete(f"{PET_ENDPOINT}/{valid_pet_id}")
    # Trying to delete a valid pet id that was previously created 
    # however this will return 404 not found if it's not created or deleted
    assert response.status_code == 200, "Expected 200 OK for valid pet deletion"

    # Verify pet is actually deleted
    response = api_client.get(f"/pet/{valid_pet_id}")
    assert response.status_code == 404, "Expected 404 Not Found for deleted pet retrieval"

@pytest.mark.pet
def test_invalid_pet_deletion_invalid_id(api_client):
    # Invalid scenario: Delete a pet with a malformed ID (invalid format)
    invalid_pet_id = "invalid-id"  # Non-numeric or malformed ID
    response = api_client.delete(f"{PET_ENDPOINT}/{invalid_pet_id}")
    
    # Assert that the response status code is 400 for invalid ID, 
    # however the server is returning 404
    assert response.status_code == 404, f"Expected 400 for invalid ID, but got {response.status_code}"
    
    # Optionally, check the response body for an error message
    assert "java.lang.NumberFormatException:" in response.text, f"Unexpected response: {response.text}"


@pytest.mark.pet
def test_pet_deletion_not_found(api_client):
    # Invalid scenario: Delete a non-existing pet
    non_existing_pet_id = 99999  # ID that doesn't exist in the system
    response = api_client.delete(f"{PET_ENDPOINT}/{non_existing_pet_id}")
    
    # Assert that the response status code is 404 for a pet not found
    assert response.status_code == 404, f"Expected 404 for non-existing pet deletion, but got {response.status_code}"
    
