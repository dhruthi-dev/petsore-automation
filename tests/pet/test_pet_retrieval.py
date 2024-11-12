import pytest
from src.framework.endpoints import PET_BY_ID_ENDPOINT, PET_FIND_BY_STATUS_ENDPOINT
from tests.data.test_data import valid_pet_status, invalid_pets_data, minimal_pets_data

@pytest.mark.pet
@pytest.mark.parametrize("pet_data", minimal_pets_data)
def test_pet_retrieval_by_valid_id(api_client, pet_data):
    # Valid scenario: Retrieve an existing pet by valid ID - 11113
    # Note that this should be created as a part of create tests, not deleted
    pet_id = pet_data["id"]
    response = api_client.get(PET_BY_ID_ENDPOINT.format(petId=pet_id))
    assert response.status_code == 200, "Expected 200 OK for valid pet retrieval"
    assert response.json()["id"] == pet_id, "Expected pet ID to match"

@pytest.mark.pet
def test_pet_retrieval_by_id_invalid_id(api_client):
    # Invalid scenario: Attempt to retrieve pet by malformed string ID
    response = api_client.get(PET_BY_ID_ENDPOINT.format(petId={invalid_pets_data[0]["id"]}))
    assert response.status_code == 404, "Expected 404 Not Found for invalid pet retrieval"

@pytest.mark.pet
def test_pet_retrieval_by_id_pet_not_found(api_client):
    # Invalid scenario: Attempt to retrieve pet by invalid/non-existent ID
    response = api_client.get(PET_BY_ID_ENDPOINT.format(petId={invalid_pets_data[1]["id"]}))
    assert response.status_code == 404, "Expected 404 Not Found for invalid pet retrieval"

@pytest.mark.pet
@pytest.mark.parametrize("pet_status", valid_pet_status)
def test_pet_retrieval_by_status_valid(api_client, pet_status):
    # Valid scenario: Retrieve an existing pet by ID
    response = api_client.find_pet_by_status(pet_status)
    print(response.text)
    assert response.status_code == 200, "Encountered unexpected status for valid pet retrieval"
    assert response.json() != None, "Expected to have a big list of matching entries"

@pytest.mark.pet
@pytest.mark.xfail(reason="This should return 400, but it's returning 200")
def test_pet_retrieval_by_status_invalid(api_client):
    # Invalid scenario: Retrieve a non-existing pet
    response = api_client.get(f"{PET_FIND_BY_STATUS_ENDPOINT}?status=abcdefghi")
    # BUG: This should return failure error code, but returning 200
    assert response.status_code == 400, "Expected status code Not Found for invalid pet retrieval"
    assert response.json() == []
