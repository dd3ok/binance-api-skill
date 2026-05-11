# Filters And Enums

Use this for validating order parameters before `TRADE` calls. Always verify current symbol rules through `GET /api/v3/exchangeInfo`; local notes and copied formulas are not runtime truth.

## Decimal Safety

Use `Decimal`, integer scaled units, or an exchange/library helper. Do not use binary floating point for price, quantity, tick-size, step-size, or notional validation.

## Common Symbol Filters

| Filter | Validate |
| --- | --- |
| `PRICE_FILTER` | `price`/`stopPrice` within min/max and aligned to `tickSize` |
| `PERCENT_PRICE` | price within multiplier range around average/reference price |
| `PERCENT_PRICE_BY_SIDE` | side-specific price multiplier range |
| `LOT_SIZE` | `quantity`/`icebergQty` within min/max and aligned to `stepSize` |
| `MARKET_LOT_SIZE` | market order quantity rules |
| `MIN_NOTIONAL` | minimum `price * quantity`, sometimes applied to market orders |
| `NOTIONAL` | minimum and maximum notional range |
| `ICEBERG_PARTS` | maximum iceberg parts |
| `MAX_NUM_ORDERS` | symbol-level open order limit |
| `MAX_NUM_ALGO_ORDERS` | symbol-level algo order limit |

## Validation Pattern

1. Fetch `GET /api/v3/exchangeInfo?symbol=...` for the target environment.
2. Parse filters by `filterType`.
3. Quantize price and quantity using decimal-safe math.
4. Validate notional after quantization.
5. Fail closed on unknown `filterType`; do not silently ignore filters not implemented by the client.
6. Use `/api/v3/order/test` on Testnet before live placement.

## Official Docs To Fetch

- `filters.md`
- `enums.md`
- REST heading `Exchange information`
- REST heading `Query relevant filters (USER_DATA)` when applicable
- Price range execution rules FAQ when percent-price filters matter
