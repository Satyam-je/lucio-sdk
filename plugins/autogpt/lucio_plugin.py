"""
Lucio AutoGPT Plugin
Built by Artéfacts, Inc.

This plugin demonstrates how Lucio can be
integrated into agent workflows.

It replaces direct credential usage with
temporary authorization tokens.
"""

import os

from autogpt.plugins import AutoGPTPluginTemplate
from lucio import LucioClient


class LucioPlugin(AutoGPTPluginTemplate):

    _name = "LucioPlugin"
    _version = "0.1.0"
    _description = (
        "Lucio integration for AutoGPT agents."
    )

    def __init__(self):
        super().__init__()

        enterprise_key = os.getenv(
            "LUCIO_ENTERPRISE_KEY"
        )

        if not enterprise_key:
            raise ValueError(
                "LUCIO_ENTERPRISE_KEY not found."
            )

        self.client = LucioClient(
            enterprise_key
        )

    def can_handle_pre_command(self) -> bool:
        return True

    def pre_command(
        self,
        command_name: str,
        arguments: dict
    ):

        agent_id = arguments.get(
            "agent_id",
            "autogpt_agent"
        )

        token = self.client.authenticate(
            agent_id=agent_id,
            action=command_name
        )

        arguments["lucio_token"] = token

        sensitive_fields = [
            "api_key",
            "password",
            "secret",
            "token",
            "credential",
            "private_key",
            "access_key"
        ]

        for field in sensitive_fields:

            if field in arguments:
                del arguments[field]

        return (
            command_name,
            arguments
        )

    def can_handle_post_command(self) -> bool:
        return True

    def post_command(
        self,
        command_name: str,
        response: str
    ):

        return response
