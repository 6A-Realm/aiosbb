# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__ = "Commands"

from aiosbb import SBBClient


async def getTitleID(client: SBBClient) -> str:
    """Get the title ID of the current game.

    This method sends the `getTitleID` command to the SBB device and returns the response. The response is a string containing the title ID of the current game.

    Args:
        client: An SBBClient object.

    Returns:
        The title ID of the current game, as a string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getTitleID"
    result = await client(command)
    return result