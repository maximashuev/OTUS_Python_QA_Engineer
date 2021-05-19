import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default=200,
        help="This is request status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def st_code(request):
    return request.config.getoption("--status_code")


def test_module1(url, st_code):
    response = requests.get(url)
    assert response.status_code == st_code
