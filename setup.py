# setup.py
from setuptools import setup, find_packages

setup(
    name="petstore-automation",
    version="0.1",
    packages=find_packages(where="src"),  # Specify the src directory
    package_dir={"": "src"},              # Map the src directory as the root
)
