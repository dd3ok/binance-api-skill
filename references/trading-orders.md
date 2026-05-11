# Trading Orders

Use this only for `TRADE` endpoint implementation or debugging. Prefer Spot Testnet and require explicit confirmation before live trading.

## Live Trading Gate

Before any live `TRADE` call, confirm all of:

- Environment is live, not testnet.
- Endpoint, relevant FAQ/changelog, and official docs section were checked in this session.
- API key has the required permission and is intentionally live.
- Symbol, side, order type, quantity, price or quote quantity, time in force, `newClientOrderId`, and `recvWindow`.
- Current `exchangeInfo` filters, account balances, and rate/order-count limits were checked.
- The user understands that API mechanics are not investment advice.

If confirmation is missing, provide code or commands for Testnet or `/api/v3/order/test` only.

## Common Endpoint Families

| Need | Endpoint family | Official heading |
| --- | --- | --- |
| Validate order without placement | `POST /api/v3/order/test` | `Test new order (TRADE)` |
| Place order | `POST /api/v3/order` | `New order (TRADE)` |
| Cancel order | `DELETE /api/v3/order` | `Cancel order (TRADE)` |
| Cancel all open orders | `DELETE /api/v3/openOrders` | `Cancel All Open Orders on a Symbol (TRADE)` |
| Cancel and replace | `POST /api/v3/order/cancelReplace` | `Cancel an Existing Order and Send a New Order (TRADE)` |
| Amend keep priority | `PUT /api/v3/order/amend/keepPriority` | `Order Amend Keep Priority (TRADE)` |
| Order lists | `/api/v3/orderList/*` | `Order lists` |

## Unknown Execution Status

For `5XX`, `-1006`, or `-1007` after order operations, do not blindly retry. Execution status may be unknown. Query order status and/or use User Data Stream guidance.

## Official Docs To Fetch

- REST heading `Trading endpoints`
- Specific order endpoint heading
- REST heading `HTTP Return Codes`
- REST heading `Request Security`
- `filters.md` and `exchangeInfo` for validation
- Trading FAQs such as `order_count_decrement`, `market_orders_faq`, `stp_faq`, `sor_faq`, and order amend/pegged order FAQs when relevant
