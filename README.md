# Lucio SDK
**by Darpan, Inc.**

> No vault. Nothing stored. Nothing to steal.

Lucio is an AI that tokenizes any signing credential and permanently discards the original. Every authentication happens fresh at the moment of use. Nothing sits anywhere to be stolen.

Drift lost $285M. Bybit lost $1.4B. Kelp DAO lost $292M. Same root cause every time — stored credentials.

Lucio eliminates that attack surface entirely.

---

## How it works

```
Traditional agent:         API_KEY = "sk-abc123"  ← sitting there, waiting to be stolen
                           
With Lucio:                token = lucio.authenticate(agent_id, action)  ← one-time, then gone
```

Your agent never sees or stores the credential. Lucio's AI processes it on Darpan's servers, returns a one-time token valid for that single action only, then permanently discards everything.

---

## Install

```bash
pip install lucio-sdk
```

---

## Quick start

```python
import lucio

# Initialize once
lucio.init(enterprise_key="your_enterprise_key")

# Authenticate any agent action — no credential stored anywhere
token = lucio.authenticate(
    agent_id="my_agent",
    action="send_email"
)

# Token used once, then permanently gone
```

---

## AutoGPT Plugin

```python
# Add to your AutoGPT .env
LUCIO_ENTERPRISE_KEY=your_enterprise_key

# Add to your plugins list
from plugins.autogpt.lucio_plugin import LucioPlugin
```

That's it. Every agent command is automatically intercepted and credentials replaced with one-time Lucio tokens. Nothing stored in your agent config ever again.

---

## Architecture

```
┌─────────────────────────────────────────┐
│  OPEN SOURCE (this repo)                │
│  ┌─────────────────────────────────┐    │
│  │  Lucio SDK                      │    │
│  │  lucio.authenticate()           │    │
│  │  lucio.verify()                 │    │
│  │  lucio.revoke()                 │    │
│  └──────────────┬──────────────────┘    │
└─────────────────┼───────────────────────┘
                  │ API call
┌─────────────────▼───────────────────────┐
│  PROPRIETARY (Darpan servers)           │
│  ┌─────────────────────────────────┐    │
│  │  Lucio AI Core                  │    │
│  │  Tokenization engine (E=W·X)    │    │
│  │  Credential processing          │    │
│  │  Permanent discard              │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

The integration layer is fully open source — audit it, fork it, contribute to it.
The core AI model runs on Darpan's servers — that's where the magic happens.

---

## Enterprise

Lucio is a B2B enterprise product. Pricing is based on assets secured.

Contact: **partnerships@darpan.io**

---

## License

MIT — open source integration layer only.
Core model is proprietary to Darpan, Inc.
