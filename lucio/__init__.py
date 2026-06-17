"""
Lucio SDK
Built by Artéfacts, Inc.

Public SDK layer for communicating with a Lucio
authorization server.

The SDK handles:
- Authentication requests
- Token verification
- Token revocation

Backend infrastructure remains separate.
"""

import os
import requests
from typing import Optional


#
# API URL
#

LUCIO_API_URL = os.getenv(
    "LUCIO_API_URL",
    "https://YOUR_SERVER_URL_HERE"
)


class LucioClient:
    """
    Main Lucio client.
    """

    def __init__(self, enterprise_key: str):

        self.enterprise_key = enterprise_key

        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"Bearer {enterprise_key}",
            "Content-Type": "application/json"
        })

    def authenticate(
        self,
        agent_id: str,
        action: str,
        scope: Optional[str] = None
    ) -> str:

        response = self.session.post(
            f"{LUCIO_API_URL}/authenticate",
            json={
                "agent_id": agent_id,
                "action": action,
                "scope": scope
            }
        )

        response.raise_for_status()

        return response.json()["token"]

    def verify(
        self,
        token: str,
        action: str
    ) -> bool:

        response = self.session.post(
            f"{LUCIO_API_URL}/verify",
            json={
                "token": token,
                "action": action
            }
        )

        response.raise_for_status()

        return response.json().get(
            "valid",
            False
        )

    def revoke(
        self,
        agent_id: str
    ) -> bool:

        response = self.session.post(
            f"{LUCIO_API_URL}/revoke",
            json={
                "agent_id": agent_id
            }
        )

        response.raise_for_status()

        return response.json().get(
            "revoked",
            False
        )


#
# Global client
#

_client = None


def init(
    enterprise_key: str
):
    """
    Initialize Lucio.

    Example:
        lucio.init("my_key")
    """

    global _client

    _client = LucioClient(
        enterprise_key
    )


def authenticate(
    agent_id: str,
    action: str,
    scope: Optional[str] = None
):

    if _client is None:
        raise RuntimeError(
            "Call lucio.init() first."
        )

    return _client.authenticate(
        agent_id=agent_id,
        action=action,
        scope=scope
    )


def verify(
    token: str,
    action: str
):

    if _client is None:
        raise RuntimeError(
            "Call lucio.init() first."
        )

    return _client.verify(
        token=token,
        action=action
    )


def revoke(
    agent_id: str
):

    if _client is None:
        raise RuntimeError(
            "Call lucio.init() first."
        )

    return _client.revoke(
        agent_id=agent_id
    )
