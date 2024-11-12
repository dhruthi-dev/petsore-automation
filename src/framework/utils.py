import os
from pathlib import Path

# method to return the status code of a response
def assert_status_code(response, expected_code):
    assert response.status_code == expected_code, \
        f"Expected status {expected_code}, but got {response.status_code}"

# method to return the response in the form of json  
def get_json(response):
    return response.json() if response.headers.get("Content-Type") == "application/json" else None

# method to get the full path to the image files
def get_image_file_path(file_name):
    # project_root = Path(__file__).parent.parent.resolve()
    # target_path = os.path.join(os.path.dirname(__file__), 'images', file_name)
    # return os.path.relpath(target_path, project_root)
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Define the absolute path to the images directory
    images_dir = os.path.join(current_dir, 'tests', 'data', 'images', file_name)
    
    # Get the relative path from the current working directory to the images directory
    relative_path = os.path.relpath(images_dir, current_dir)
    
    return relative_path

