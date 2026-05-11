# Account Endpoints

Use this for signed account, order status, and trade history endpoints. Verify the exact official endpoint section and `USER_DATA` security before implementation.

## Requirements

- These endpoints generally require `X-MBX-APIKEY`, `timestamp`, and `signature`.
- Load `auth-signing.md` before coding signed calls.
- Never print account balances, order IDs, or signed URLs unless the user requested the output and secrets are masked.

## Common Endpoint Families

| Need | Endpoint | Official heading |
| --- | --- | --- |
| Account balances and permissions | `GET /api/v3/account` | `Account information (USER_DATA)` |
| Query order | `GET /api/v3/order` | `Query order (USER_DATA)` |
| Current open orders | `GET /api/v3/openOrders` | `Current open orders (USER_DATA)` |
| All orders | `GET /api/v3/allOrders` | `All orders (USER_DATA)` |
| Order list status | `GET /api/v3/orderList` | `Query Order list (USER_DATA)` |
| All order lists | `GET /api/v3/allOrderList` | `Query all Order lists (USER_DATA)` |
| Open order lists | `GET /api/v3/openOrderList` | `Query Open Order lists (USER_DATA)` |
| Account trades | `GET /api/v3/myTrades` | `Account trade list (USER_DATA)` |
| Order count | `GET /api/v3/rateLimit/order` | `Query Unfilled Order Count (USER_DATA)` |
| Commission rates | `GET /api/v3/account/commission` | `Query Commission Rates (USER_DATA)` |

## Operational Notes

- For order status after uncertain trading errors, query by `orderId` or `origClientOrderId` as official docs allow.
- Handle time windows and pagination explicitly; do not assume full account history is returned by default.
- Include request weight awareness for batch or repeated account queries.
- User Data Stream is adjacent WebSocket behavior, not REST coverage. Mention it only when real-time account/order updates or unknown execution recovery matter.

## Official Docs To Fetch

- REST heading `Account Endpoints`
- Specific endpoint heading
- REST heading `Request Security`
- REST heading `LIMITS`
- Commission FAQ when explaining commission fields
