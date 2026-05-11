#!/usr/bin/env python3
"""Verify Binance-style HMAC-SHA-256 signature payloads locally."""

from __future__ import annotations

import hashlib
import hmac
import os
import sys


SELF_TEST_SECRET = "sample-secret"
SELF_TEST_EXAMPLES = [
    (
        "ascii-order",
        "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559",
        "12c8598c73734da90faa25e7fe433fe0709d285bb25537b84338a5d0ca1e0f8d",
    ),
    (
        "encoded-non-ascii-symbol",
        "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559",
        "9d0b84d1d03a955fd64041bcb57fefdd3a761b128829bce2053820a2a07cbd75",
    ),
]


def sign(secret: str, payload: str) -> str:
    return hmac.new(secret.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256).hexdigest()


def main() -> int:
    if len(sys.argv) > 1:
        print("usage: verify_hmac_signature.py", file=sys.stderr)
        print("Set BINANCE_HMAC_TEST_SECRET, BINANCE_HMAC_TEST_PAYLOAD, and optional BINANCE_HMAC_TEST_EXPECTED for custom non-secret tests.", file=sys.stderr)
        return 2

    secret = os.environ.get("BINANCE_HMAC_TEST_SECRET")
    payload = os.environ.get("BINANCE_HMAC_TEST_PAYLOAD")
    expected = os.environ.get("BINANCE_HMAC_TEST_EXPECTED")
    if secret or payload or expected:
        if not (secret and payload):
            print("error: BINANCE_HMAC_TEST_SECRET and BINANCE_HMAC_TEST_PAYLOAD must be set together", file=sys.stderr)
            return 2
        actual = sign(secret, payload)
        print(actual)
        if expected and actual.lower() != expected.lower():
            print("signature mismatch", file=sys.stderr)
            return 1
        return 0

    failures = 0
    for name, payload, expected in SELF_TEST_EXAMPLES:
        actual = sign(SELF_TEST_SECRET, payload)
        ok = actual.lower() == expected.lower()
        print(f"{name}: {'ok' if ok else 'fail'}")
        if not ok:
            print(f"  expected {expected}", file=sys.stderr)
            print(f"  actual   {actual}", file=sys.stderr)
            failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
