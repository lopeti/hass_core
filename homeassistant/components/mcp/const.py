"""Constants for the Model Context Protocol integration."""

DOMAIN = "mcp"

CONF_ACCESS_TOKEN = "access_token"
CONF_AUTHORIZATION_URL = "authorization_url"
CONF_TOKEN_URL = "token_url"

# Transport types
CONF_TRANSPORT = "transport"
TRANSPORT_SSE = "sse"
TRANSPORT_STREAMABLE_HTTP = "streamable_http"
DEFAULT_TRANSPORT = TRANSPORT_SSE
