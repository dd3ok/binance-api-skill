# Errors And Limits

Use this for HTTP errors, Binance error payloads, request weight, order count, WAF behavior, and retry/backoff. Verify exact current limits in official docs and `exchangeInfo`.

## HTTP Statuses

| Status | Meaning |
| --- | --- |
| `4XX` | Request problem on sender side |
| `403` | WAF/security rule violation; can relate to rate limits or blocked request content |
| `409` | Cancel-replace partially succeeded |
| `418` | IP auto-banned after repeated limit violations |
| `429` | Request rate limit exceeded |
| `5XX` | Binance-side error; execution status may be unknown |

## Rate Limit Rules

- Design around request weight, not raw request count.
- Inspect `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` response headers.
- Inspect `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` for order count where present.
- Use `GET /api/v3/exchangeInfo` `rateLimits` as runtime truth for current configured limits.
- On `429` or `418`, respect `Retry-After` and back off.
- Limits are IP-based for request weight; unfilled order count is account-based.
- Do not hardcode numeric limits from examples without checking current docs or `exchangeInfo`.

## Error Payloads

Binance errors usually look like:

```json
{"code": -1121, "msg": "Invalid symbol."}
```

Codes are stable; messages may vary.

## High-Risk Codes

| Code | Meaning |
| --- | --- |
| `-1003` | Too many requests / request weight / possible ban |
| `-1006` | Unexpected response; execution status unknown |
| `-1007` | Timeout; execution status unknown |
| `-1015` | Too many new orders |
| `-1021` | Invalid timestamp / outside `recvWindow` |
| `-1022` | Invalid signature |
| `-1121` | Invalid symbol |

## Official Docs To Fetch

- REST heading `HTTP Return Codes`
- REST heading `LIMITS`
- `errors.md`
- `faqs/order_count_decrement.md`
- FAQ/rate-limit/WAF support article
