---
name: binance-api-skill
description: "Use when implementing/debugging Binance Spot REST /api/* calls: /api/v3 market data, signed account/orders, API keys, HMAC/RSA/Ed25519 signing, recvWindow, filters, rate limits, errors, or Testnet."
---

# Binance API

Use this skill for Binance API work centered on Spot REST `/api/*`. For Futures `/fapi`, Delivery `/dapi`, Margin, Wallet `/sapi`, FIX, SBE, or WebSocket APIs, state that this Spot REST workflow does not apply; do not adapt Spot endpoints, filters, or order rules.

## Operating Principles

- Stay inside Spot REST `/api/*`; reject non-Spot scopes instead of adapting Spot patterns.
- Treat official Binance docs and `GET /api/v3/exchangeInfo` as authoritative; use local references only for routing.
- Prefer the lowest-risk path that satisfies the task: public/read-only endpoints first, Spot Testnet before live `TRADE`.
- When exact execution, filters, signing, or rate-limit behavior cannot be verified, disclose uncertainty instead of asserting it.

## Workflow

1. Start from `references/index.md` and load only the references needed for the task.
2. Treat local references as routing notes, not source of truth. Before implementing or calling an endpoint where exact parameters, request weights, security type, signing, filters, or order behavior matter, fetch the relevant official Binance documentation section first.
3. Re-check official docs on errors, API changes, rate-limit behavior, live trading, or any mismatch between local notes and observed behavior.
4. If official docs cannot be fetched, disclose that exact behavior could not be verified, avoid live trading guidance, and do not assert current parameters, weights, security types, or filters.
5. Prefer public market-data endpoints when the task does not require account state. Prefer Spot Testnet for trading examples.
6. Do not provide financial advice. Keep responses about API mechanics, validation, and operational risk.

## Official Sources

Use these in priority order:

- Binance Spot REST docs: `https://developers.binance.com/docs/binance-spot-api-docs/rest-api`
- Official GitHub docs and changelog: `https://github.com/binance/binance-spot-api-docs`
- Runtime exchange rules: `GET /api/v3/exchangeInfo`
- Binance developer forum for troubleshooting only: `https://dev.binance.vision`
- FAQ/WAF/rate-limit support context: `https://www.binance.com/en/support/faq/detail/360004492232`

For exact Markdown sections, use `scripts/extract_official_section.py` against raw GitHub docs.

## Reference Map

- `references/rest-core.md`: base URLs, request placement, time units, data ordering, data sources.
- `references/endpoints.md`: current compact Spot REST `/api/v3` endpoint catalog.
- `references/auth-signing.md`: security types, API keys, signatures, timestamp, `recvWindow`.
- `references/market-data.md`: public endpoints such as `/time`, `/exchangeInfo`, `/klines`, tickers, depth.
- `references/trading-orders.md`: `TRADE` endpoints and live-order safety gates.
- `references/account-endpoints.md`: signed account and order history endpoints.
- `references/filters-enums.md`: symbol filters, order validation, decimal-safe arithmetic.
- `references/errors-limits.md`: HTTP codes, Binance error codes, request weight, bans, unknown execution.
- `references/testnet.md`: Spot Testnet base URL and constraints.

## Safety Rules

- Never ask the user to paste secrets. Use environment variables and mask keys in logs.
- Default to read-only public market data when the user intent does not require account state or trading.
- Never run live `TRADE` calls unless the user explicitly requested live trading and confirmed the exact symbol, side, type, quantity, price rules, and environment.
- For `5XX` or `-1007 TIMEOUT` after order operations, do not assume failure. Query order status or use User Data Stream guidance.
- On `429` or `418`, back off and respect `Retry-After`; repeated violations can trigger IP bans.
- Use `Decimal` or equivalent fixed-precision math for `PRICE_FILTER`, `LOT_SIZE`, and notional checks.

## Response Checklist

Before final answer, confirm:

- Scope is Spot REST `/api/*`, or non-Spot scope is clearly rejected.
- Official docs or runtime rules were checked when exact behavior matters, or uncertainty is disclosed.
- No secrets, live-trade execution, or financial advice are exposed.
- Endpoint, auth/signing needs, request weight/rate-limit notes, and failure caveats are included when relevant.

## Example

User: "Implement BTCUSDT 1h klines."

Do: load `references/market-data.md`, fetch the official `/api/v3/klines` section, use a public endpoint, include request weight and time-range assumptions, and avoid auth/signing.
