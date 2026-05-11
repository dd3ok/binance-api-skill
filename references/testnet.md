# Spot Testnet

Use Spot Testnet or Demo Mode for examples that could place, cancel, or modify orders. These environments reduce financial risk but do not remove the need to validate filters, signing, and rate limits.

## Base URL

- REST base prefix: `https://testnet.binance.vision/api`
- Example full URL: `https://testnet.binance.vision/api/v3/time`
- Testnet supports Spot `/api/*` endpoints. Do not assume `/sapi/*` support.
- Demo Mode docs live under `demo-mode/` in the official GitHub repo. Check Demo Mode when the user needs an environment closer to live features or realistic market data.

## Safety Workflow

1. Use separate Spot Testnet credentials.
2. Fetch testnet `GET /api/v3/exchangeInfo` for current symbols and filters.
3. Use `/api/v3/order/test` before any actual testnet order.
4. Keep request weights and backoff behavior in place on testnet.
5. Consider Demo Mode when Testnet lacks a feature or live-like market behavior is important.
6. Make live trading an explicit, separate step.

## Differences To Mention

- Testnet funds are virtual.
- Testnet state and availability may differ from live.
- Live API keys and Testnet API keys are separate.
- Validate exact endpoint support in the current Testnet docs.
- Testnet and Demo Mode have separate docs and changelogs; check the matching environment docs.

## Official Docs To Fetch

- Testnet REST docs: `testnet/rest-api.md`
- Testnet website: `https://testnet.binance.vision/`
- Demo Mode docs: `demo-mode/general-info.md`
