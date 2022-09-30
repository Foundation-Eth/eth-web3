from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from utils_eth.curried import (
    apply_formatter_if,
    apply_formatters_to_dict,
    apply_key_map,
    is_null,
)
from utils_eth.toolz import (
    complement,
    compose,
)
from hexbytes import (
    HexBytes,
)

from eth_web3._utils.rpc_abi import (
    RPC,
)
from eth_web3.middleware.formatting import (
    async_construct_formatting_middleware,
    construct_formatting_middleware,
)
from eth_web3.types import (
    AsyncMiddleware,
    RPCEndpoint,
)

if TYPE_CHECKING:
    from eth_web3 import Web3  # noqa: F401

is_not_null = complement(is_null)

remap_geth_poa_fields = apply_key_map(
    {
        "extraData": "proofOfAuthorityData",
    }
)

pythonic_geth_poa = apply_formatters_to_dict(
    {
        "proofOfAuthorityData": HexBytes,
    }
)

geth_poa_cleanup = compose(pythonic_geth_poa, remap_geth_poa_fields)


geth_poa_middleware = construct_formatting_middleware(
    result_formatters={
        RPC.eth_getBlockByHash: apply_formatter_if(is_not_null, geth_poa_cleanup),
        RPC.eth_getBlockByNumber: apply_formatter_if(is_not_null, geth_poa_cleanup),
    },
)


async def async_geth_poa_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
) -> AsyncMiddleware:
    middleware = await async_construct_formatting_middleware(
        result_formatters={
            RPC.eth_getBlockByHash: apply_formatter_if(is_not_null, geth_poa_cleanup),
            RPC.eth_getBlockByNumber: apply_formatter_if(is_not_null, geth_poa_cleanup),
        },
    )
    return await middleware(make_request, w3)
