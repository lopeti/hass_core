"""Test the Streamable HTTP handshake."""

import httpx
import respx

from homeassistant.components.mcp.config_flow import validate_input
from homeassistant.components.mcp.const import (
    CONF_TRANSPORT,
    CONF_URL,
    TRANSPORT_STREAMABLE_HTTP,
)
from homeassistant.core import HomeAssistant


@respx.mock
async def test_streamable_http_handshake(hass: HomeAssistant) -> None:
    """Ensure GET and POST are issued during handshake."""
    url = "http://example.com/mcp"

    respx.get(url).mock(
        return_value=httpx.Response(200, headers={"Mcp-Session-Id": "abc"})
    )
    respx.post(url).mock(
        return_value=httpx.Response(
            200,
            json={
                "result": {
                    "serverInfo": {"name": "test"},
                    "capabilities": {"tools": [1]},
                }
            },
        )
    )

    result = await validate_input(
        hass,
        {CONF_URL: url, CONF_TRANSPORT: TRANSPORT_STREAMABLE_HTTP},
    )

    assert respx.calls.call_count == 2
    assert result["title"] == "test"
