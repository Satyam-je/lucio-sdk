"""
Lucio SDK Example
Built by Artéfacts, Inc.
"""

import lucio

lucio.init(
    enterprise_key="YOUR_ENTERPRISE_KEY"
)

token = lucio.authenticate(
    agent_id="agent_001",
    action="send_email"
)

print("Generated Token:")
print(token)

valid = lucio.verify(
    token=token,
    action="send_email"
)

print("Valid:")
print(valid)

revoked = lucio.revoke(
    agent_id="agent_001"
)

print("Revoked:")
print(revoked)
