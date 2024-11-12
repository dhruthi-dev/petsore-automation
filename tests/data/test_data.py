# tests/test_data.py
from src.framework.utils import get_image_file_path

# Sample test data for dogs (Tommy and Angela)
valid_pets_data = [
    {
        "id": 11111,
        "category": {
            "id": 11111,
            "name": "Dog"
        },
        "name": "Tommy",
        "photoUrls": [
            get_image_file_path("tommy.png"),
        ],
        "tags": [
            {
                "id": 11111,
                "name": "dog"
            }
        ],
        "status": "available"
    },
    {
        "id": 11112,
        "category": {
            "id": 11112,
            "name": "Dog"
        },
        "name": "Angela",
        "photoUrls": [
            get_image_file_path("angela.png"),
        ],
        "tags": [
            {
                "id": 11112,
                "name": "dog"
            }
        ],
        "status": "sold"
    }
] 

minimal_pets_data = [
    {
        "id": 11113,
        "name": "Benny",
        "status": "pending"
    }
]

invalid_pets_data = [
    {
        "id": "abc", 
        "name": 11111,
        "tags1": 1,
        "status": "abc"
    },
    {
        "id": 99999000, # non-esistant pet-id
        "name": "tom",
        "tags1": 1,
        "status": "sold"
    },
    {
        "id": 123,  # Valid pet ID but missing some required fields
        "name": "",  # Name is empty, which should trigger a validation exception
        "status": "available"
    }
]

update_pets_data = [
    {
        "id": 11111,
        "name": "Tommy labrador",
        "status": "available"
    }
]

valid_pet_status = ["available", "pending", "sold"]

# Order Data for Testing
valid_order_data = [
    {
        "id": 1,
        "petId": 123456,
        "quantity": 1,
        "shipDate": "2024-11-11T13:48:55.004Z",
        "status": "placed",
        "complete": True
    }
]

invalid_order_data = [
    {
        "id": 0000,
        "petId": None,
        "quantity": "ABC",
        "status": 1,
        "complete": "not_a_boolean"
    }
]

# User Data for Testing
valid_user_data = [
    {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
]

invalid_user_data = [
    {
        "id": 0000,
        "username": 1,
        "firstName": None,
        "lastName": "ABC",
        "email": "not_an_email",
        "password": 1122,
        "phone": "not_a_phone_number",
        "userStatus": "not_a_status"
    }
]


