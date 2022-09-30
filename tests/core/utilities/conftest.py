import pytest

from eth_web3.main import (
    Web3,
)
from eth_web3.providers.eth_tester import (
    EthereumTesterProvider,
)


@pytest.fixture(scope="module")
def w3():
    provider = EthereumTesterProvider()
    return Web3(provider)
