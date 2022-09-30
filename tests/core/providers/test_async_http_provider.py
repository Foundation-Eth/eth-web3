import pytest

from aiohttp import (
    ClientSession,
)

from eth_web3._utils import (
    request,
)
from eth_web3.providers.async_rpc import (
    AsyncHTTPProvider,
)


@pytest.mark.asyncio
async def test_user_provided_session() -> None:
    session = ClientSession()
    provider = AsyncHTTPProvider(endpoint_uri="http://mynode.local:8545")
    cached_session = await provider.cache_async_session(session)
    assert len(request._async_session_cache) == 1
    assert cached_session == session
