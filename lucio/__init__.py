"""
Lucio SDK — Open Source Integration Layer
by Darpan, Inc.

The core tokenization model runs on Darpan's servers.
This SDK is the open source integration layer only.
Nothing is stored locally. Ever.
"""

import requests
import os
from typing import Optional

LUCIO_API_URL = os.getenv("LUCIO_API_URL", "https://api.darpan.io/v1")

class LucioClient:
    def __init__(self, enterprise_key: str):
        """
        Initialize Lucio with your enterprise API key.
        
        Args:
            enterprise_key: Your Darpan enterprise key (contact partnerships@darpan.io)
        """
        self.enterprise_key = enterprise_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {enterprise_key}",
            "Content-Type": "application/json"
        })

    def authenticate(self, agent_id: str, action: str, scope: Optional[str] = None) -> str:
        """
        Authenticate an agent action without storing any credential.
        
        The credential is tokenized and permanently discarded on Darpan's servers.
        Nothing is stored anywhere — not locally, not remotely.
        
        Args:
            agent_id: Unique identifier for your AI agent
            action: The action the agent is performing (e.g. "send_email", "sign_transaction")
            scope: Optional scope to limit the authorization
            
        Returns:
            A one-time use authorization token valid for this single action only
            
        Example:
            token = lucio.authenticate(agent_id="my_agent", action="send_email")
        """
        response = self.session.post(f"{LUCIO_API_URL}/authenticate", json={
            "agent_id": agent_id,
            "action": action,
            "scope": scope
        })
        response.raise_for_status()
        return response.json()["token"]

    def verify(self, token: str, action: str) -> bool:
        """
        Verify a one-time token is valid for a given action.
        
        Args:
            token: The token returned by authenticate()
            action: The action to verify
            
        Returns:
            True if valid, False otherwise
        """
        response = self.session.post(f"{LUCIO_API_URL}/verify", json={
            "token": token,
            "action": action
        })
        return response.json().get("valid", False)

    def revoke(self, agent_id: str) -> bool:
        """
        Immediately revoke all active tokens for an agent.
        
        Args:
            agent_id: The agent to revoke
            
        Returns:
            True if successful
        """
        response = self.session.post(f"{LUCIO_API_URL}/revoke", json={
            "agent_id": agent_id
        })
        return response.json().get("revoked", False)


# Convenience singleton — initialize once, use anywhere
_client: Optional[LucioClient] = None

def init(enterprise_key: str):
    """Initialize Lucio with your enterprise key."""
    global _client
    _client = LucioClient(enterprise_key)

def authenticate(agent_id: str, action: str, scope: Optional[str] = None) -> str:
    """Authenticate an agent action. Call lucio.init() first."""
    if not _client:
        raise RuntimeError("Call lucio.init(enterprise_key) first")
    return _client.authenticate(agent_id, action, scope)

def verify(token: str, action: str) -> bool:
    """Verify a token is valid."""
    if not _client:
        raise RuntimeError("Call lucio.init(enterprise_key) first")
    return _client.verify(token, action)

def revoke(agent_id: str) -> bool:
    """Revoke all tokens for an agent."""
    if not _client:
        raise RuntimeError("Call lucio.init(enterprise_key) first")
    return _client.revoke(agent_id)
