# REST Core

Use this for base URLs, request mechanics, time handling, and data freshness. Verify exact endpoint behavior in the official endpoint section before coding.

## Scope

- This skill covers Binance Spot REST `/api/*`, especially `/api/v3/*`.
- Out of scope by default: Futures `/fapi`, Delivery `/dapi`, Options `/eapi`, Margin/Wallet/Sub-account `/sapi`, WebSocket API, WebSocket streams, FIX, and SBE.
- User Data Stream is adjacent WebSocket behavior. Mention it for timeout/order-status recovery, but do not treat it as Spot REST endpoint coverage.

## Base URLs

- Stable REST base: `https://api.binance.com`
- Alternate REST bases: `https://api-gcp.binance.com`, `https://api1.binance.com`, `https://api2.binance.com`, `https://api3.binance.com`, `https://api4.binance.com`
- Public market-data-only REST base: `https://data-api.binance.vision`
- Spot Testnet REST base prefix: `https://testnet.binance.vision/api`; example full URL: `https://testnet.binance.vision/api/v3/time`

Use market-data-only URLs for unauthenticated public data when possible.

## Request Rules

- `GET` parameters go in the query string.
- `POST`, `PUT`, and `DELETE` parameters may be sent in the query string or `application/x-www-form-urlencoded` body.
- If a parameter appears in both query and body, the query parameter wins.
- Responses are JSON by default.
- JSON timestamps are milliseconds by default. Microseconds require `X-MBX-TIME-UNIT: MICROSECOND` or `microsecond`.

## Data Ordering And Sources

- Without `startTime` or `endTime`, many endpoints return the most recent items up to `limit`.
- With `startTime`, many endpoints return oldest items from `startTime` up to `limit`.
- With `endTime`, many endpoints return the most recent items up to `endTime` and `limit`.
- Endpoints may identify data source as Matching Engine, Memory, or Database. Matching Engine is generally freshest; Database may lag.

## Official Docs To Fetch

- REST general info: `rest-api.md` heading `General API Information`
- Data sources: `rest-api.md` heading `Data Sources`
- Changelog: `CHANGELOG.md`
- Market data only FAQ: `faqs/market_data_only.md`
