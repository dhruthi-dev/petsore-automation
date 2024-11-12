# Pet store API Automation Framework
This contains pytest automation for petstore swagger link - https://petstore.swagger.io/#/

## Project Structure
```plaintext
pet-api-automation/
├── src/
│   ├── api_client.py           # Defines API client methods
│   ├── config.py               # Configuration file for API details
│   └── utils.py                # Helper utilities, like data generation
├── tests/
│   ├── test_pet_endpoint.py    # Test suite for the /pet endpoint
│   ├── conftest.py             # Fixtures for test setup/teardown
│   └── data/
│       └── pet_data.json       # Test data
├── requirements.txt            # Required dependencies
└── pytest.ini                  # Pytest configuration
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
2. Use the provided API client (PetApiClient in src/api_client.py) and fixtures from conftest.py for test setup and teardown.
3. Follow the naming convention test_<feature>.py and add methods prefixed with test_ for pytest to recognize them.

