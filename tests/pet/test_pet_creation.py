import pytest
from src.framework.endpoints import PET_ENDPOINT
from src.framework.utils import *
from tests.data.test_data import valid_pets_data, invalid_pets_data, minimal_pets_data

@pytest.mark.pet
@pytest.mark.parametrize("pet_data", valid_pets_data + minimal_pets_data)
def test_create_valid_pet(api_client, pet_data):
    response = api_client.post(PET_ENDPOINT, data=pet_data)
    assert_status_code(response, 200)
    pet = response.json()
    assert pet["name"] == pet_data["name"], "Pet name does not match"
    assert pet["status"] == pet_data["status"], "Pet status does not match"

@pytest.mark.pet
@pytest.mark.xfail(reason="server is preventing from passing invalid name and id field, returning 500 error")
def test_create_invalid_pet(api_client):
     # Bug: this will create the pet and return 200 status code when id is valid, but other fields are invaild
    response = api_client.post(PET_ENDPOINT, data=invalid_pets_data[0])
    # check that it's returning 4xx error
    assert response.status_code == 405, f"Expected 400 error status, got {response.status_code}"
   
@pytest.mark.pet
@pytest.mark.parametrize("pet_data", valid_pets_data)
def test_upload_pet_image(api_client, pet_data):
    response = api_client.upload_pet_image("uploading pet image", pet_data["photoUrls"][0], pet_data["id"])
    print(response.text)
    assert_status_code(response, 200)
    assert f"uploading pet image\nFile uploaded to ./{pet_data["name"]}.png".lower() in get_json(response)["message"].lower() , \
    f"unexpected response, got {get_json(response)["message"]}"
