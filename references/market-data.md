# Market Data

Use this for public, unauthenticated Spot REST market data. Verify the exact endpoint section before implementing parameters, weights, limits, or response parsing.

## Prefer Public Bases

- General REST: `https://api.binance.com`
- Market-data-only REST: `https://data-api.binance.vision`

Use `data-api.binance.vision` only for endpoints Binance lists as market-data-only compatible.

## Common Endpoints

| Need | Endpoint | Official heading |
| --- | --- | --- |
| Connectivity | `GET /api/v3/ping` | `Test connectivity` |
| Server time | `GET /api/v3/time` | `Check server time` |
| Symbols, filters, rate limits | `GET /api/v3/exchangeInfo` | `Exchange information` |
| Order book | `GET /api/v3/depth` | `Order book` |
| Recent trades | `GET /api/v3/trades` | `Recent trades list` |
| Historical trades | `GET /api/v3/historicalTrades` | `Old trade lookup` |
| Aggregate trades | `GET /api/v3/aggTrades` | `Compressed/Aggregate trades list` |
| Candles | `GET /api/v3/klines` | `Kline/Candlestick data` |
| UI candles | `GET /api/v3/uiKlines` | `UIKlines` |
| Average price | `GET /api/v3/avgPrice` | `Current average price` |
| 24h ticker | `GET /api/v3/ticker/24hr` | `24hr ticker price change statistics` |
| Symbol price | `GET /api/v3/ticker/price` | `Symbol price ticker` |
| Best bid/ask | `GET /api/v3/ticker/bookTicker` | `Symbol order book ticker` |

## Implementation Notes

- Include the endpoint weight in code comments or docs when loops or polling are involved.
- Avoid high-frequency REST polling for live updates; WebSocket streams may be the correct adjacent API.
- For each endpoint, verify current request weight, parameters, data source, and limits in the official section.
- For relative date requests, state the assumed timezone and convert to Binance timestamps explicitly.
- Use `exchangeInfo` as runtime truth for currently listed symbols, permissions, filters, and rate limits.

## Official Docs To Fetch

- REST heading `Market Data endpoints`
- Specific endpoint heading, e.g. `Kline/Candlestick data`
- Market data only FAQ: `faqs/market_data_only.md`
