"""
Lucio Plugin for AutoGPT
by Darpan, Inc.

Replaces AutoGPT's credential storage entirely.
Agents authenticate without ever storing credentials.
"""

from autogpt.plugins import AutoGPTPluginTemplate
from lucio import LucioClient
import os


class LucioPlugin(AutoGPTPluginTemplate):
    """
    Lucio — AI credential tokenization for AutoGPT agents.
    
    Instead of storing API keys and credentials in your agent config,
    Lucio tokenizes them at the moment of use and permanently discards
    the original. Nothing stored means nothing to steal.
    
    Setup:
        1. pip install lucio-sdk
        2. Add LUCIO_ENTERPRISE_KEY to your .env
        3. Add LucioPlugin to your plugins list
    """

    _name = "LucioPlugin"
    _version = "0.1.0"
    _description = "Vaultless credential security for AutoGPT agents by Darpan Inc."

    def __init__(self):
        super().__init__()
        enterprise_key = os.getenv("LUCIO_ENTERPRISE_KEY")
        if not enterprise_key:
            raise ValueError(
                "LUCIO_ENTERPRISE_KEY not found in environment. "
                "Contact partnerships@darpan.io to get your enterprise key."
            )
        self.lucio = LucioClient(enterprise_key)

    def can_handle_pre_command(self) -> bool:
        return True

    def pre_command(self, command_name: str, arguments: dict) -> tuple[str, dict]:
        """
        Intercept every agent command and replace stored credentials
        with a one-time Lucio token before execution.
        """
        agent_id = arguments.get("agent_id", "autogpt_agent")
        
        # Get a one-time token for this specific action
        token = self.lucio.authenticate(
            agent_id=agent_id,
            action=command_name
        )
        
        # Replace any stored credential with the one-time token
        arguments["lucio_token"] = token
        
        # Remove any raw credentials from arguments
        for key in ["api_key", "password", "secret", "token", "credential"]:
            if key in arguments:
                del arguments[key]
        
        return command_name, arguments

    def can_handle_post_command(self) -> bool:
        return True

    def post_command(self, command_name: str, response: str) -> str:
        """Token is automatically invalidated after use on Darpan's servers."""
        return response
