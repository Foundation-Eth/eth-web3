import pkg_resources

from account_eth import Account  # noqa: E402,
from eth_web3.main import Web3  # noqa: E402,
from eth_web3.providers.eth_tester import (  # noqa: E402
    EthereumTesterProvider,
)
from eth_web3.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from eth_web3.providers.rpc import (  # noqa: E402
    HTTPProvider,
)
from eth_web3.providers.async_rpc import (  # noqa: E402
    AsyncHTTPProvider,
)
from eth_web3.providers.websocket import (  # noqa: E402
    WebsocketProvider,
)

__version__ = pkg_resources.get_distribution("eth_web3").version

__all__ = [
    "__version__",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "WebsocketProvider",
    "EthereumTesterProvider",
    "Account",
    "AsyncHTTPProvider",
]
