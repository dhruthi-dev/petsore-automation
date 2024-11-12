import requests 
import urllib
import json
from config import API_BASE_URL
from src.framework.endpoints import PET_UPLOAD_IMAGE_ENDPOINT, PET_FIND_BY_STATUS_ENDPOINT
import logging

# Enable logging for the requests module
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("requests").setLevel(logging.DEBUG)

class ApiClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.session = requests.Session()

    def post(self, endpoint, data=None, files=None):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(f"{self.base_url}{endpoint}", headers=headers, data=json.dumps(data), verify=False)
        logging.info(response.text)
        return response

    def put(self, endpoint, data=None):
        headers = {'Content-Type': 'application/json'}
        response = self.session.put(f"{self.base_url}{endpoint}", headers=headers, data=json.dumps(data))
        logging.info(response.text)
        return response

    def get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}{endpoint}", params=params)
        logging.info(response.text)
        return response

    def delete(self, endpoint):
        response = self.session.delete(f"{self.base_url}{endpoint}")
        logging.info(response.text)
        return response
    
    def upload_pet_image(self, additional_metadata, image_path, pet_id):
        # Open the image file for uploading
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            data = {'additionalMetadata': additional_metadata}
            headers = {'accept': 'application/json'}
            response = self.session.post(f"{self.base_url}{PET_UPLOAD_IMAGE_ENDPOINT.format(petId=pet_id)}", headers=headers, data=data, files=files)
        logging.info(response.text)
        return response
    
    def find_pet_by_status(self, pet_status):
        response = self.get(f"{PET_FIND_BY_STATUS_ENDPOINT}?status={pet_status}")
        logging.info(response.text)
        return response
    
    def update_pet_using_id(self, endpoint, pet_id, data=None):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        # Encode the data in the correct format for application/x-www-form-urlencoded
        if data:
            data = urllib.parse.urlencode(data)  # URL-encode the data

        # Log the data being sent
        logging.info(f"Sending data: {data}")

        # Send the POST request
        response = self.session.post(f"{self.base_url}{endpoint}/{pet_id}", headers=headers, data=data, verify=False)

        # Log the response text
        logging.info(f"Response: {response.text}")
        return response
    
    '''
    def add_pet(self, pet_data):
        headers = {'Content-Type': 'application/json'}
        response = self.session.post(self.base_url, headers=headers, data=json.dumps(pet_data), verify=False)
        print(f"Status Code: {response.status_code}")
        print(response.text)
        return response
    
    def update_existing_pet(self, pet_data):
        response = self.session.put(self.base_url, json=pet_data)
        return response
    
    def find_pet_by_status(self, status):
        response = self.session.get(f"{self.base_url}/'findPetByStatus'", status)
        return response

    def get_pet_by_id(self, pet_id):
        response = self.session.get(f"{self.base_url}/{pet_id}")
        return response

    def delete_pet(self, pet_id):
        response = self.session.delete(f"{self.base_url}/{pet_id}")
        return response
    '''
    
