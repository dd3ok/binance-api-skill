# Current Spot REST Endpoints

This is a compact discovery catalog for current Binance Spot REST `/api/v3` endpoints checked against the official raw `rest-api.md` on 2026-05-11. Use it to find the right official heading, then fetch that section for current parameters, weights, security type, data source, and response shape.

## General

| Method | Path | Official heading |
| --- | --- | --- |
| `GET` | `/api/v3/ping` | `Test connectivity` |
| `GET` | `/api/v3/time` | `Check server time` |
| `GET` | `/api/v3/exchangeInfo` | `Exchange information` |
| `GET` | `/api/v3/executionRules` | `Query Execution Rules` |

## Market Data

| Method | Path | Official heading |
| --- | --- | --- |
| `GET` | `/api/v3/depth` | `Order book` |
| `GET` | `/api/v3/trades` | `Recent trades list` |
| `GET` | `/api/v3/historicalTrades` | `Old trade lookup` |
| `GET` | `/api/v3/historicalBlockTrades` | `Historical Block Trades` |
| `GET` | `/api/v3/aggTrades` | `Compressed/Aggregate trades list` |
| `GET` | `/api/v3/klines` | `Kline/Candlestick data` |
| `GET` | `/api/v3/uiKlines` | `UIKlines` |
| `GET` | `/api/v3/avgPrice` | `Current average price` |
| `GET` | `/api/v3/ticker/24hr` | `24hr ticker price change statistics` |
| `GET` | `/api/v3/ticker/tradingDay` | `Trading Day Ticker` |
| `GET` | `/api/v3/ticker/price` | `Symbol price ticker` |
| `GET` | `/api/v3/ticker/bookTicker` | `Symbol order book ticker` |
| `GET` | `/api/v3/ticker` | `Rolling window price change statistics` |
| `GET` | `/api/v3/referencePrice` | `Query Reference Price` |
| `GET` | `/api/v3/referencePrice/calculation` | `Query Reference Price Calculation` |

## Trading

All trading endpoints require the live-order safety gate in `trading-orders.md`.

| Method | Path | Official heading |
| --- | --- | --- |
| `POST` | `/api/v3/order` | `New order (TRADE)` |
| `POST` | `/api/v3/order/test` | `Test new order (TRADE)` |
| `DELETE` | `/api/v3/order` | `Cancel order (TRADE)` |
| `DELETE` | `/api/v3/openOrders` | `Cancel All Open Orders on a Symbol (TRADE)` |
| `POST` | `/api/v3/order/cancelReplace` | `Cancel an Existing Order and Send a New Order (TRADE)` |
| `PUT` | `/api/v3/order/amend/keepPriority` | `Order Amend Keep Priority (TRADE)` |
| `POST` | `/api/v3/order/oco` | `New OCO - Deprecated (TRADE)` |
| `POST` | `/api/v3/orderList/oco` | `New Order list - OCO (TRADE)` |
| `POST` | `/api/v3/orderList/oto` | `New Order list - OTO (TRADE)` |
| `POST` | `/api/v3/orderList/otoco` | `New Order list - OTOCO (TRADE)` |
| `POST` | `/api/v3/orderList/opo` | `New Order List - OPO (TRADE)` |
| `POST` | `/api/v3/orderList/opoco` | `New Order List - OPOCO (TRADE)` |
| `DELETE` | `/api/v3/orderList` | `Cancel Order list (TRADE)` |
| `POST` | `/api/v3/sor/order` | `New order using SOR (TRADE)` |
| `POST` | `/api/v3/sor/order/test` | `Test new order using SOR (TRADE)` |

## Account

These are signed `USER_DATA` endpoints unless the official section says otherwise.

| Method | Path | Official heading |
| --- | --- | --- |
| `GET` | `/api/v3/account` | `Account information (USER_DATA)` |
| `GET` | `/api/v3/order` | `Query order (USER_DATA)` |
| `GET` | `/api/v3/openOrders` | `Current open orders (USER_DATA)` |
| `GET` | `/api/v3/allOrders` | `All orders (USER_DATA)` |
| `GET` | `/api/v3/orderList` | `Query Order list (USER_DATA)` |
| `GET` | `/api/v3/allOrderList` | `Query all Order lists (USER_DATA)` |
| `GET` | `/api/v3/openOrderList` | `Query Open Order lists (USER_DATA)` |
| `GET` | `/api/v3/myTrades` | `Account trade list (USER_DATA)` |
| `GET` | `/api/v3/rateLimit/order` | `Query Unfilled Order Count (USER_DATA)` |
| `GET` | `/api/v3/myPreventedMatches` | `Query Prevented Matches (USER_DATA)` |
| `GET` | `/api/v3/myAllocations` | `Query Allocations (USER_DATA)` |
| `GET` | `/api/v3/account/commission` | `Query Commission Rates (USER_DATA)` |
| `GET` | `/api/v3/order/amendments` | `Query Order Amendments (USER_DATA)` |
| `GET` | `/api/v3/myFilters` | `Query relevant filters (USER_DATA)` |

## Maintenance Rule

If a requested endpoint is missing here, check the official REST docs and changelog before saying it does not exist. If the official docs differ from this catalog, follow the official docs and update this file.
