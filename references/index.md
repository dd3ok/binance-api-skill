# Binance Spot REST Reference Index

Local references are routing notes. Use them to choose the right official Binance section, then verify exact endpoint details against official docs before implementation, live calls, or error diagnosis.

## Route By Task

| User task | Read first | Then verify official section |
| --- | --- | --- |
| Base URL, request shape, timestamps, data ordering | `rest-core.md` | REST "General API Information" and endpoint section |
| Current Spot REST endpoint discovery | `endpoints.md` | Matching REST endpoint heading and changelog |
| Public prices, candles, tickers, order book | `market-data.md` | REST "Market Data endpoints" |
| Signed account data or order history | `auth-signing.md`, `account-endpoints.md` | REST "Request Security" and "Account Endpoints" |
| New/cancel/replace/test orders | `auth-signing.md`, `trading-orders.md`, `filters-enums.md`, `testnet.md` | REST "Trading endpoints" and `GET /api/v3/exchangeInfo` |
| Signature, timestamp, `recvWindow`, API key permissions | `auth-signing.md` | REST "Request Security" and API key type FAQ |
| `429`, `418`, `403`, request weights, WAF | `errors-limits.md` | REST "LIMITS", HTTP return codes, FAQ |
| Filter failures, invalid precision, min notional | `filters-enums.md`, `errors-limits.md` | `filters.md`, `errors.md`, `exchangeInfo` |
| Spot Testnet | `testnet.md` | Spot Testnet docs |

## Core Source URLs

- REST docs: `https://developers.binance.com/docs/binance-spot-api-docs/rest-api`
- Raw REST Markdown: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md`
- Official repo: `https://github.com/binance/binance-spot-api-docs`
- Changelog: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/CHANGELOG.md`
- Enums: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/enums.md`
- Errors: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/errors.md`
- Filters: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/filters.md`
- API key types: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/api_key_types.md`
- Commission FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/commission_faq.md`
- Market data only: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/market_data_only.md`
- Market orders FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/market_orders_faq.md`
- Order count decrement FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/order_count_decrement.md`
- Order amend keep priority FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/order_amend_keep_priority.md`
- Pegged orders FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/pegged_orders.md`
- Price range execution rules FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/price_range_execution_rules.md`
- SOR FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/sor_faq.md`
- STP FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/stp_faq.md`
- Trailing stop FAQ: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/faqs/trailing-stop-faq.md`
- Testnet REST: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/rest-api.md`
- Demo Mode info: `https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/demo-mode/general-info.md`
- FAQ/rate-limit/WAF: `https://www.binance.com/en/support/faq/detail/360004492232`

Check the changelog before relying on current or edge behavior, especially trading endpoints, account endpoints, filters, and rate limits.

## Official Section Helper

```bash
python3 scripts/extract_official_section.py \
  --url https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md \
  --heading "Kline/Candlestick data"
```
