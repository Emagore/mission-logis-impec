"""Config flow pour Mission Logis Impec."""
from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow

from .const import DOMAIN


class MissionLogisImpecConfigFlow(ConfigFlow, domain=DOMAIN):
    """Un seul écran, aucun champ : confirme et crée l'entrée."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> Any:
        if user_input is not None:
            return self.async_create_entry(title="Mission Logis Impec", data={})

        return self.async_show_form(step_id="user")
