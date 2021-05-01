"""Python interface for TP-Link's smart home devices.

All common, shared functionalities are available through `SmartDevice` class::

    x = SmartDevice("192.168.1.1")
    print(x.sys_info)

For device type specific actions `SmartBulb`, `SmartPlug`, or `SmartStrip`
 should be used instead.

Module-specific errors are raised as `SmartDeviceException` and are expected
to be handled by the user of the library.
"""
from importlib_metadata import version  # type: ignore
from .kasa.auth import Auth
from .kasa.exceptions import SmartDeviceException
from .kasa.protocol import TPLinkSmartHomeProtocol
from .kasa.smartdevice import DeviceType, EmeterStatus, SmartDevice
from .kasa.smartplug import SmartPlug

__version__ = "0.4.0.dev2"

__all__ = [
    "Auth",
    "TPLinkSmartHomeProtocol",
    "DeviceType",
    "EmeterStatus",
    "SmartDevice",
    "SmartDeviceException",
    "SmartPlug"
]
