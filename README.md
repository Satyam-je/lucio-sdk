Lucio SDK

Built by Artéfacts, Inc.

Lucio is a lightweight Python SDK for integrating token-based authorization, agent authentication, and secure action verification into AI systems, automation workflows, and enterprise applications.

The SDK provides a simple interface for communicating with a Lucio authorization server while keeping implementation details abstracted behind a clean API.

---

Installation

pip install lucio-sdk

---

Quick Start

import lucio

lucio.init(
    enterprise_key="YOUR_ENTERPRISE_KEY"
)

token = lucio.authenticate(
    agent_id="agent_001",
    action="send_email"
)

print(token)

---

Authentication

Request a temporary authorization token.

token = lucio.authenticate(
    agent_id="agent_001",
    action="send_email"
)

---

Verification

Verify whether a token is valid for a specific action.

valid = lucio.verify(
    token=token,
    action="send_email"
)

---

Revocation

Invalidate active authorization tokens.

lucio.revoke(
    agent_id="agent_001"
)

---

Configuration

Lucio automatically reads the API endpoint from the environment.

export LUCIO_API_URL=https://YOUR_SERVER_URL_HERE

If not specified, the SDK uses the default value defined in "lucio/__init__.py".

---

Repository Structure

lucio-sdk/
├── README.md
├── setup.py
├── .gitignore
├── lucio/
│   └── __init__.py
├── plugins/
│   └── autogpt/
│       └── lucio_plugin.py
└── examples/
    └── example.py

---

AutoGPT Integration

The repository includes an AutoGPT plugin that demonstrates how Lucio can be integrated into agent-based systems.

from plugins.autogpt.lucio_plugin import LucioPlugin

---

Development Status

Current version:

v0.1.0-alpha

This repository contains the public SDK layer.

Server-side infrastructure, authorization engines, and deployment configurations are maintained separately.

---

Support

support@YOUR_DOMAIN_HERE

---

Documentation

https://YOUR_DOMAIN_HERE/docs

---

License

MIT License

Copyright (c) Artéfacts, Inc.
