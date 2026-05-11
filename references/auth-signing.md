# Auth And Signing

Use this for signed requests, API key permissions, timestamps, and signature mechanics. Always verify official Request Security docs before implementing a signed endpoint.

## Security Types

| Type | Meaning |
| --- | --- |
| `NONE` | Public market data |
| `TRADE` | Place, cancel, or modify orders |
| `USER_DATA` | Private account/order/trade data |
| `USER_STREAM` | User Data Stream subscription management |

Except where Binance says otherwise, non-`NONE` endpoints are signed and require `X-MBX-APIKEY`.

## Signed Request Checklist

- Send API key in `X-MBX-APIKEY`.
- Include `timestamp` in milliseconds or microseconds.
- Include `signature` in the query string or request body.
- Keep `recvWindow` small; default is 5000 ms and maximum is 60000 ms.
- Call `/api/v3/time` or otherwise handle clock skew when diagnosing `-1021`.
- Prefer separate least-privilege keys for read-only, account, and trading work.
- Do not log secrets or full signed URLs in a way that exposes credentials.
- Confirm the endpoint security type in official docs before coding.

## Key Types

Binance supports Ed25519, HMAC, and RSA keys. Binance's API key type FAQ recommends Ed25519 for performance and security. HMAC examples are common, but do not assume HMAC is the only supported signing mode.

## HMAC Notes

- Signature payload is the query string concatenated directly with the HTTP body, without an extra separator.
- Percent-encode non-ASCII characters before signing.
- HMAC payload and secret are case-sensitive; the resulting hex signature is not case-sensitive.
- Use `scripts/verify_hmac_signature.py` to verify HMAC payload construction locally with your own non-secret test values.

RSA and Ed25519 are supported but require their official examples or connector-library support. Do not adapt the HMAC helper for asymmetric keys.

## Official Docs To Fetch

- REST heading `Request Security`
- REST heading `SIGNED Endpoint security`
- REST heading `SIGNED Endpoint Examples for POST /api/v3/order`
- API key type FAQ: `faqs/api_key_types.md`
