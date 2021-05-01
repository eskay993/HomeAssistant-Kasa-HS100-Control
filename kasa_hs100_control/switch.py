"""Kasa HS100 Plug Home Assistant Intergration"""
import logging
import voluptuous as vol
import asyncio
from .kasa.auth import Auth
from .kasa.smartplug import SmartPlug
from .kasa.exceptions import SmartDeviceException

import homeassistant.helpers.config_validation as cv

from homeassistant.components.switch import SwitchEntity
from homeassistant.const import CONF_HOST, CONF_USERNAME, CONF_PASSWORD
from homeassistant.components.switch import PLATFORM_SCHEMA

import json

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
	vol.Required(CONF_HOST): cv.string,
	vol.Required(CONF_USERNAME): cv.string,
	vol.Required(CONF_PASSWORD): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
	# Assign configuration variables.
	# The configuration check takes care they are present.
	host = config[CONF_HOST]
	username = config[CONF_USERNAME]
	password = config.get(CONF_PASSWORD)

	# Setup connection with devices/cloud
	hs100 = asyncio.run(klapp(host, username, password))
	if hs100 != None:
		add_entities([HS100Plug(hs100)])


async def klapp(host, username, password):
	# Connect to device using TP-Link KLAPP protocol
	try:
		plug = SmartPlug(host, Auth(username, password))
		await plug.update()
		return plug
	except SmartDeviceException as err:
		_LOGGER.error(err)
		return None


class HS100Plug(SwitchEntity):
	"""Representation of a HS100 Plug"""

	def __init__(self, hs100):
		self._hs100 = hs100
		asyncio.run(self._hs100.update())
		self._name = self._hs100.alias
		self._is_on = self._hs100.is_on

	@property
	def name(self):
		"""Name of the device."""
		return self._name

	@property
	def is_on(self):
		"""Device State"""
		return self._is_on

	def turn_on(self, **kwargs) -> None:
		"""Turn hs100 On"""
		asyncio.run(self._hs100.turn_on())
		asyncio.run(self._hs100.update())
		self._is_on = True

	def turn_off(self, **kwargs):
		"""Turn hs100 Off"""
		asyncio.run(self._hs100.turn_off())		
		asyncio.run(self._hs100.update())
		self._is_on = False
