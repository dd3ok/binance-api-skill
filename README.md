# Binance API Skill

Unofficial Codex/OpenAI skill for Binance Spot REST API work. This repository packages a `SKILL.md`, focused references, and small helper scripts so coding agents can implement or debug Binance Spot REST `/api/*` calls with official Binance docs, endpoint routing, signed requests, API keys, HMAC/RSA/Ed25519 signing, `recvWindow`, filters, request weights, rate limits, errors, and Testnet safety in mind.

This is not an official Binance project and does not provide financial advice.

## Scope

- Covered: Binance Spot REST `/api/*`, especially `/api/v3` market data, signed account endpoints, order endpoints, filters, errors, and Spot Testnet.
- Not covered: Futures `/fapi`, Delivery `/dapi`, Margin, Wallet `/sapi`, WebSocket APIs, FIX, or SBE. The skill tells agents not to adapt Spot REST rules to those APIs.
- Source of truth: official Binance documentation and runtime `GET /api/v3/exchangeInfo`; local references are routing notes.

## Install

Clone this repository into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/dd3ok/binance-api-skill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/binance-api-skill"
```

Restart Codex after installing so the skill can be discovered.

This repository root is intentionally the installable Codex skill package. Runtime skill files are `SKILL.md`, `agents/openai.yaml`, `references/`, and `scripts/`; `README.md` and `LICENSE` are repository-facing files for public GitHub distribution.

## Usage

Example prompt:

```text
Use $binance-api-skill to implement BTCUSDT 1h klines with official Binance docs.
```

Good pressure prompts:

- `Implement BTCUSDT 1h klines in Python.`
- `Why am I getting -1022 invalid signature?`
- `I got -1007 after POST /api/v3/order. Should I retry?`
- `Use /fapi/v1/order for Binance futures.`
- `Place a live BTCUSDT market buy order.`

Expected behavior: the agent should verify official docs for exact behavior, prefer public market data when possible, refuse or gate live trading, avoid secret exposure, and reject non-Spot REST scope instead of translating Spot rules to other Binance APIs.

## Contents

- `SKILL.md`: trigger metadata, workflow, safety rules, and response checklist.
- `references/index.md`: task-to-reference routing.
- `references/endpoints.md`: compact `/api/v3` endpoint discovery snapshot.
- `references/*.md`: focused notes for signing, market data, trading, account endpoints, filters, errors, limits, and Testnet.
- `scripts/extract_official_section.py`: prints one section from official Binance Spot docs.
- `scripts/verify_hmac_signature.py`: local HMAC payload self-test and non-secret test helper.
- `evals/prompts.md`: manual pressure prompts for maintainers.

## Official Sources

- Binance Spot REST docs: https://developers.binance.com/docs/binance-spot-api-docs/rest-api
- Official Binance Spot API docs repo: https://github.com/binance/binance-spot-api-docs
- Binance developer forum: https://dev.binance.vision
- Binance API FAQ/rate-limit/WAF context: https://www.binance.com/en/support/faq/detail/360004492232

## License

MIT. This license applies to this repository's original skill files and helper scripts, not to Binance documentation, trademarks, or services.
