Lucio SDK

by Artéfacts, Inc.

«No vault. Nothing stored. Nothing to steal.»

Lucio is a credential authorization platform designed for AI agents, automation systems, and enterprise workflows.

Instead of relying on long-lived credentials that remain stored indefinitely, Lucio generates authorization tokens at the moment of use and validates access through a centralized authorization layer.

---

Features

- Token-based authorization
- Agent authentication
- Permission validation
- Token verification
- Token revocation
- Enterprise integration support
- AutoGPT plugin support
- Open-source SDK
- Private backend architecture

---

Installation

pip install lucio-sdk

---

Quick Start

import lucio

lucio.init(
    enterprise_key="your_enterprise_key"
)

token = lucio.authenticate(
    agent_id="agent_001",
    action="send_email"
)

print(token)

---

Verify

valid = lucio.verify(
    token=token,
    action="send_email"
)

print(valid)

---

Revoke

lucio.revoke(
    agent_id="agent_001"
)

---

Environment Variable

The SDK automatically reads:

LUCIO_API_URL

Example:

export LUCIO_API_URL=https://YOUR_SERVER_URL_HERE

---

Architecture

Application
      │
      ▼
Lucio SDK
      │
      ▼
Lucio API
      │
      ▼
Authorization Engine

The SDK is open source.

Backend infrastructure remains private.

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

Company

Artéfacts, Inc.

For enterprise inquiries:

partnerships@artefacts.ai

---

License

MIT License
