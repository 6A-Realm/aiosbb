# SPDX-License-Identifier: MIT

"""
aiosbb: Asynchronous sys-botbase client/server framework in Python.

This framework provides a simple and easy-to-use way to control sys-botbase devices from Python. It uses an asynchronous API, which makes it ideal for use in long-running tasks or with multiple devices.

To use the framework, simply create a new `SBBClient` object and send commands to the device using the `__call__()` method. The framework will handle the connection and communication with the device, and return the responses to your commands.

For more information, please see the documentation at https://github.com/6A-Realm/aiosys-botbase
"""

__title__ = "aiosbb"
__author__ = "Z1R343L, 6A-Realm"
__license__ = "MIT"
__copyright__ = "Copyright 2023-present Z1R343L"
__version__ = "0.1.1"

from .sbbclient import SBBClient

