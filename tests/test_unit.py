import python_api


def test_pytest_runs():
    assert python_api.module_exists()
