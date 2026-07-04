import asyncio
import logging

from homeassistant.core import HomeAssistant

from .const import DOMAIN, HOST, PORT

_LOGGER = logging.getLogger(__name__)


async def async_setup_services(hass: HomeAssistant):

    async def flash_id(call):

        cmd = [
            "python3",
            "-m",
            "esptool",
            "--port",
            f"rfc2217://{HOST}:{PORT}",
            "flash-id",
        ]

        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )

        stdout, _ = await proc.communicate()

        _LOGGER.warning(stdout.decode())

    hass.services.async_register(
        DOMAIN,
        "flash_id",
        flash_id,
    )
