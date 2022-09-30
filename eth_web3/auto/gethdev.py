from eth_web3 import (
    IPCProvider,
    Web3,
)
from eth_web3.middleware import (
    geth_poa_middleware,
)
from eth_web3.providers.ipc import (
    get_dev_ipc_path,
)

w3 = Web3(IPCProvider(get_dev_ipc_path()))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
