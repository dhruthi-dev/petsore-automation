import pytest 
import sys
import os
from src.framework.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    """Fixture to initialize the ApiClient."""
    return ApiClient()

def pytest_report_header(config):
    # This will add a custom header to the test report
    return "Custom Report Header: Pet Store Automated Regression Testing Suite - v1.0"

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # This will add custom summary information at the end of the report
    passed = len(terminalreporter.stats.get("passed", []))
    xfailed = len(terminalreporter.stats.get("xfailed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))
    
    terminalreporter.write("\n")
    terminalreporter.write(f"--- Custom Summary ---\n")
    terminalreporter.write(f"Total Tests Passed: {passed} + {xfailed}\n")
    terminalreporter.write(f"Total Tests Failed: {failed}\n")
    terminalreporter.write(f"Total Tests Skipped: {skipped}\n")
    terminalreporter.write(f"Exit Status: {exitstatus}\n")
    
    if exitstatus == 0:
        terminalreporter.write("All tests passed!\n")
    else:
        terminalreporter.write("Some tests failed. Please review the report.\n")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "Pet API Testing"
        config._metadata["Module"] = "Pet API"
        config._metadata["Tester"] = "Dhruthi"
    config.addinivalue_line(
        "markers", "pet: Tests related to the pet API"
    )

@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    # Hook that executes after all tests have finished
    print("End of test suite. Clean up any resources here if needed.")
