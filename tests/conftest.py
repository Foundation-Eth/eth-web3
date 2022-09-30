import pytest

from utils_eth import (
    to_bytes,
)
from utils_eth.toolz import (
    identity,
)

from .utils import (
    get_open_port,
)


@pytest.fixture(scope="module", params=[lambda x: to_bytes(hexstr=x), identity])
def address_conversion_func(request):
    return request.param


@pytest.fixture()
def open_port():
    return get_open_port()


def pytest_addoption(parser):
    parser.addoption("--flaky", action="store_true")
