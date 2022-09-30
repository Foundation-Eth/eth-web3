from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from utils_eth import (
    is_dict,
)
from utils_eth.toolz import (
    assoc,
)

from eth_web3.datastructures import (
    AttributeDict,
)
from eth_web3.types import (
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from eth_web3 import Web3  # noqa: F401


def attrdict_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    """
    Converts any result which is a dictionary into an a
    """

    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        response = make_request(method, params)

        if "result" in response:
            result = response["result"]
            if is_dict(result) and not isinstance(result, AttributeDict):
                return assoc(response, "result", AttributeDict.recursive(result))
            else:
                return response
        else:
            return response

    return middleware
