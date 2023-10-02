# SPDX-License-Identifier: MIT

__all__ = "ipv4_pattern"

from re import compile


"""IPv4 regex used to validate IP addresses.
Matches any string in the format `XXX.XXX.XXX.XXX`, where each `X` is a digit from 0 to 255.
"""
ipv4_pattern = compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

