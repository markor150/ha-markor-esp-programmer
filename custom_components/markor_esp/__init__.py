"""MarKor ESP Programmer."""
from .services import async_setup_services

async def async_setup(hass, config):
    await async_setup_services(hass)
    return True
