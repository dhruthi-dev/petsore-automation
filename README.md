# Pet store API Automation Framework
This contains pytest automation for petstore swagger link - https://petstore.swagger.io/#/

## Project Structure
```plaintext
petstore-automation/
│
├── src/
│   ├── framework/                # Core framework for API interactions and test utilities
│   │   ├── __init__.py
│   │   ├── api_client.py         # API client to make requests to the PetStore API
│   │   ├── endpoints.py          # Contains endpoint URLs for the PetStore API
│   │   └── utils.py              # Utility functions used across tests
│   │
│   ├── config.py                 # Configuration file for the project (e.g., base URLs, settings)
│   └── __init__.py               # Marks the directory as a Python package
│
├── tests/
│   ├── data/                     # Contains test data for different scenarios
│   │   └── test_data.py          # Test data for pets and invalid data
│   │
│   ├── pet/                      # Pet-related tests
│   │   ├── test_pet_creation.py  # Tests for creating pets and updating images
│   │   ├── test_pet_update.py    # Tests for updating pet details
│   │   ├── test_pet_deletion.py  # Tests for deleting pets
│   │   └── test_pet_retrieval.py # Tests for retrieving pet details
│   └── __init__.py               # Marks the directory as a Python package
│   └── conftest.py               # Contains pytest hooks and fixtures
│
├── pytest.ini                    # Pytest configuration file
└── requirements.txt              # Project dependencies
```
## Pre-requisites 
Python 3.7+
pip for package management

## Clone the repository:
git clone https://github.com/dhruthi-dev/petsore-automation.git
cd petsore-automation

## Create and Activate a Virtual Environment:
python3 -m venv petstore_venv
source petstore_venv/bin/activate    # On macOS/Linux
petstore_venv\Scripts\activate       # On Windows

## Install this project in editable mode:
pip install -e .

## Install External Dependencies:
pip install -r requirements.txt

## Running the Tests
To run all tests execute the command - `pytest`
To run specific test execute the command - `pytest -k <testname>`
To run tests in a specific group execute the command - `pytest -m <marker name>`

## Writing New Tests
1. Create a new test file in the tests/ directory.
2. Use the provided API client (PetApiClient in api_client.py) and fixtures from conftest.py for test setup and teardown.
3. Follow the naming convention test_<feature>.py and add methods prefixed with test_ for pytest to recognize them.

