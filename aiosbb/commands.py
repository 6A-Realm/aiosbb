# SPDX-License-Identifier: MIT

from __future__ import annotations

__all__ = "Commands"

# Docs: https://github.com/olliz0r/sys-botbase/blob/master/commands.md

from aiosbb import SBBClient

"""RAM Single Reading"""
async def peak(client: SBBClient, offset: int, size: int) -> str:
    """Reads memory at given address relative to heap.

    This method sends the `peak` command to the sys-botbase device and returns the response. The response is hex string containing the RAM memory.

    Args:
        client: An SBBClient object.
        offset: A hexadecimal address.
        size: The amount of bytes to read.

    Returns:
        The memory at given address relative to heap, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"peak {offset:x} {size:d}"
    result = await client(command)
    return result

async def peekAbsolute(client: SBBClient, offset: int, size: int) -> str:
    """Reads memory at given absolute address.

    This method sends the `peekAbsolute` command to the sys-botbase device and returns the response. The response is hex string containing the RAM memory.

    Args:
        client: An SBBClient object.
        offset: A hexadecimal address.
        size: The amount of bytes to read.

    Returns:
        The memory at given address, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"peekAbsolute {offset:x} {size:d}"
    result = await client(command)
    return result

async def peekMain(client: SBBClient, offset: int, size: int) -> str:
    """Reads memory at given address relative to NSOMain.

    This method sends the `peekMain` command to the sys-botbase device and returns the response. The response is hex string containing the RAM memory.

    Args:
        client: An SBBClient object.
        offset: A hexadecimal address.
        size: The amount of bytes to read.

    Returns:
        The memory at given address relative to NSOMain, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"peekMain {offset:x} {size:d}"
    result = await client(command)
    return result

"""RAM Multi Reading"""
async def peekMulti(client: SBBClient, *args) -> str:
    """Reads memory at given addresses relative to heap.

    This method sends the `peekMulti` command to the sys-botbase device and returns the response. The response is hex string containing the RAM memory.

    Args:
        client: An SBBClient object.
        *args: A list of tuples containing the addresses and sizes to read. Each tuple should have two elements:
            * The address to read from, in hexadecimal.
            * The amount of bytes to read.

    Returns:
        The memory at given addresses relative to heap, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "peekMulti "
    for address, size in args:
        command += f"{address:x} {size:d} "
    result = await client(command)
    return result

async def peekAbsoluteMulti(client: SBBClient, *args) -> str:
    """Reads memory at given absolute addresses.

    This method sends the `peekAbsoluteMulti` command to the sys-botbase device and returns the response. The response is hex string containing the RAM memory.

    Args:
        client: An SBBClient object.
        *args: A list of tuples containing the addresses and sizes to read. Each tuple should have two elements:
            * The address to read from, in hexadecimal.
            * The amount of bytes to read.

    Returns:
        The memory at given absolute addresses, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "peekAbsoluteMulti "
    for address, size in args:
        command += f"{address:x} {size:d} "
    result = await client(command)
    return result

async def peekMainMulti(client: SBBClient, *args) -> str:
    """Reads memory at given addresses relative to NSOMain.

    This method sends the `peekMainMulti` command to the sys-botbase device and returns the response. The response is hex string containing the RAM memory.

    Args:
        client: An SBBClient object.
        *args: A list of tuples containing the addresses and sizes to read. Each tuple should have two elements:
            * The address to read from, relative to NSOMain, in hexadecimal.
            * The amount of bytes to read.

    Returns:
        The memory at given addresses relative to NSOMain, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "peekMainMulti "
    for address, size in args:
        command += f"{address:x} {size:d} "
    result = await client(command)
    return result

"""Pointer Reads"""
async def pointerPeek(client: SBBClient, amount_of_bytes: int, *pointers: int) -> str:
    """Follows a chain of pointers and reads the final value.

    This method sends the `pointerPeek` command to the sys-botbase device with the given pointers and returns the response. The response is hex string containing the final value.

    Args:
        client: An SBBClient object.
        amount_of_bytes: The amount of bytes to read from the final value.
        *pointers: A list of hexadecimal addresses, representing the chain of pointers to follow.

    Returns:
        The final value, as a hex string.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"pointerPeek {amount_of_bytes:d}"
    for pointer in pointers:
        command += f" {pointer:x}"
    result = await client(command)
    return result

async def pointerPeekMulti(client: SBBClient, amount_of_bytes: int, *chains: tuple) -> str:
    """Follows a chain of pointers and reads the final value for each chain.

    This method sends the `pointerPeekMulti` command to the sys-botbase device with the given chains and returns the response. The response is a string containing the final values for each chain, separated by newline characters.

    Args:
        client: An SBBClient object.
        amount_of_bytes: The amount of bytes to read from the final value.
        *chains: A list of tuples, where each tuple represents a chain of pointers to follow.

    Returns:
        A string containing the final values for each chain, separated by newline characters.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"pointerPeekMulti {amount_of_bytes:d}"
    for chain in chains:
        for pointer in chain:
            command += f" {pointer:x}"
    result = await client(command)
    return result

async def pointer(client: SBBClient, *pointers: int) -> str:
    """Follows a chain of pointers and prints the final absolute address.

    This method sends the `pointer` command to the sys-botbase device with the given pointers and prints the final absolute address to the console.

    Args:
        client: An SBBClient object.
        *pointers: A list of hexadecimal addresses, representing the chain of pointers to follow.
    """
    command = f"pointer"
    for pointer in pointers:
        command += f" {pointer:x}"
    result = await client(command)
    print(result)

async def pointerAll(client: SBBClient, *pointers: int) -> str:
    """Follows a chain of pointers and prints the final absolute address, allowing adding a final offset without jumping.

    This method sends the `pointerAll` command to the sys-botbase device with the given pointers and prints the final absolute address to the console, with the given final offset added.

    Args:
        client: An SBBClient object.
        *pointers: A list of hexadecimal addresses, representing the chain of pointers to follow.

    Returns:
        The final absolute address, with the given final offset added.
    """
    command = f"pointerAll"
    for pointer in pointers:
        command += f" {pointer:x}"
    result = await client(command)
    print(result)

async def pointerRelative(client: SBBClient, *pointers: int, final_offset: int = 0) -> str:
    """Follows a chain of pointers and prints the final address relative to the heap, allowing adding a final offset without jumping.

    This method sends the `pointerRelative` command to the sys-botbase device with the given pointers and final offset and prints the final address relative to the heap to the console.

    Args:
        client: An SBBClient object.
        *pointers: A list of hexadecimal addresses, representing the chain of pointers to follow.
        final_offset: The final offset to add to the final address.

    Returns:
        The final address relative to the heap, with the given final offset added.
    """
    command = f"pointerRelative"
    for pointer in pointers:
        command += f" {pointer:x}"
    command += f" {final_offset:x}"
    result = await client(command)
    print(result)

"""Single Write"""
async def poke(client: SBBClient, address: int, data: int) -> str:
    """Writes bytes to given address relative to heap.

    This method sends the `poke` command to the sys-botbase device with the given address and data and returns the response.

    Args:
        client: An SBBClient object.
        address: The address to write to relative to the heap, in hexadecimal.
        data: The data to write, in hexadecimal.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"poke {address:x} {data:x}"
    result = await client(command)
    return result

async def pokeAbsolute(client: SBBClient, address: int, data: int) -> str:
    """Writes bytes to given absolute address.

    This method sends the `pokeAbsolute` command to the sys-botbase device with the given address and data and returns the response.

    Args:
        client: An SBBClient object.
        address: The absolute address to write to, in hexadecimal.
        data: The data to write, in hexadecimal.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"pokeAbsolute {address:x} {data:x}"
    result = await client(command)
    return result

async def pokeMain(client: SBBClient, address: int, data: int) -> str:
    """Writes bytes to given address relative to NSOMain.

    This method sends the `pokeMain` command to the sys-botbase device with the given address and data and returns the response.

    Args:
        client: An SBBClient object.
        address: The address to write to relative to NSOMain, in hexadecimal.
        data: The data to write, in hexadecimal.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"pokeMain {address:x} {data:x}"
    result = await client(command)
    return result

"""Pointer Write"""
async def pointerPoke(client: SBBClient, data: int, *pointers: int) -> str:
    """Writes bytes to address resulting of following a pointer chain.

    This method sends the `pointerPoke` command to the sys-botbase device with the given data and pointers and returns the response.

    Args:
        client: An SBBClient object.
        data: The bytes to write, in hexadecimal.
        *pointers: A list of hexadecimal addresses, representing the chain of pointers to follow.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"pointerPoke {data:x}"
    for pointer in pointers:
        command += f" {pointer:x}"
    result = await client(command)
    return result

"""Freezing of values"""
async def freeze(client: SBBClient, address: int, value: int, interval: int = 200) -> str:
    """Freezes a value in RAM.

    This method sends the `freeze` command to the sys-botbase device with the given address, value, and interval and returns the response.

    Args:
        client: An SBBClient object.
        address: The absolute address to freeze, in hexadecimal.
        value: The value to freeze it to, in hexadecimal.
        interval: The number of milliseconds to wait between writing to the frozen value.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"freeze {address:x} {value:x} {interval:d}"
    result = await client(command)
    return result

async def unfreeze(client: SBBClient, address: int) -> str:
    """Unfreezes a previously frozen value in RAM.

    This method sends the `unfreeze` command to the sys-botbase device with the given address and returns the response.

    Args:
        client: An SBBClient object.
        address: The absolute address to unfreeze, in hexadecimal.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"unfreeze {address:x}"
    result = await client(command)
    return result

async def freezeCount(client: SBBClient) -> str:
    """Returns number of frozen addresses in RAM."""
    command = "freezeCount"
    result = await client(command)
    return result

async def freezeClear(client: SBBClient) -> str:
    """Unfreezes all values in RAM."""
    command = "freezeClear"
    result = await client(command)
    return result

async def freezePause(client: SBBClient) -> str:
    """Pauses the freezing process."""
    command = "freezePause"
    result = await client(command)
    return result

async def freezeUnpause(client: SBBClient) -> str:
    """Unpauses a previously paused freezing of all values."""
    command = "freezeUnpause"
    result = await client(command)
    return result

"""Controller Input"""
async def press(client: SBBClient, button_type: str) -> str:
    """Presses and holds a button.

    This method sends the `press` command to the sys-botbase device with the given button type and returns the response.

    Args:
        client: An SBBClient object.
        button_type: The type of button to press.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "press"
    command += f" {button_type}"
    result = await client(command)
    return result

async def release(client: SBBClient, button_type: str) -> str:
    """Releases a button from being pressed.

    This method sends the `release` command to the sys-botbase device with the given button type and returns the response.

    Args:
        client: An SBBClient object.
        button_type: The type of button to release.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "release"
    command += f" {button_type}"
    result = await client(command)
    return result

async def click(client: SBBClient, button_type: str) -> str:
    """Holds a button pressed and releases it after a configured period of time (default 50ms).

    This method sends the `click` command to the sys-botbase device with the given button type and returns the response.

    Args:
        client: An SBBClient object.
        button_type: The type of button to click.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "click"
    command += f" {button_type}"
    result = await client(command)
    return result

async def setStick(client: SBBClient, stick_side: str, x_val: int, y_val: int) -> str:
    """Sets stick position.

    This method sends the `setStick` command to the sys-botbase device with the given stick side, X value, and Y value and returns the response.

    Args:
        client: An SBBClient object.
        stick_side: The side of the stick to set. Valid values are `LEFT` and `RIGHT`.
        x_val: The X value of the stick position.
        y_val: The Y value of the stick position.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "setStick"
    command += f" {stick_side:s} {x_val:d} {y_val:d}"
    result = await client(command)
    return result

async def clickSeq(client: SBBClient, commands: str) -> str:
    """Sends several button inputs and wait commands in sequence.

    This method sends the `clickSeq` command to the sys-botbase device with the given string of comma-separated commands and returns the response.

    Args:
        client: An SBBClient object.
        commands: A string with comma-separated commands out of the following:

        **buttonType** for click
        **+buttonType** for press
        **-buttonType** for release
        **Wnumber** to sleep number ms
        **%X,Y** move left stick to position X Y
        **&X,Y** move right stick to position X Y

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "clickSeq"
    command += commands
    result = await client(command)
    return result

async def clickCancel(client: SBBClient) -> str:
    """Interrupts click sequence.

    This method sends the `clickCancel` command to the sys-botbase device and returns the response.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "clickCancel"
    result = await client(command)
    return result

async def detachController(client: SBBClient) -> str:
    """Forces the virtual controller to detach, useful in cases where it bugs out.

    This method sends the `detachController` command to the sys-botbase device and returns the response.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "detachController"
    result = await client(command)
    return result

"""Touch Screen Input"""
async def touch(client: SBBClient, *coordinates: int) -> str:
    """Sequential taps to the touchscreen.

    This method sends the `touch` command to the sys-botbase device with the given coordinates and returns the response.

    Args:
        client: An SBBClient object.
        *coordinates: A list of X and Y coordinates, in the range 0-1280 and 0-720, respectively.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "touch"
    for coordinate in coordinates:
        command += f" {coordinate:d}"
    result = await client(command)
    return result

async def touchHold(client: SBBClient, x: int, y: int, milliseconds: int) -> str:
    """Single tap to hold.

    This method sends the `touchHold` command to the sys-botbase device with the given coordinates and milliseconds to hold and returns the response.

    Args:
        client: An SBBClient object.
        x: The X coordinate, in the range 0-1280.
        y: The Y coordinate, in the range 0-720.
        milliseconds: The number of milliseconds to hold the touch for.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "touchHold"
    command += f" {x:d} {y:d} {milliseconds:d}"
    result = await client(command)
    return result

async def touchDraw(client: SBBClient, *coordinates: int) -> str:
    """Moves the touch from given position to the next, effectively drawing on the touchscreen.

    This method sends the `touchDraw` command to the sys-botbase device with the given coordinates and returns the response.

    Args:
        client: An SBBClient object.
        *coordinates: A list of X and Y coordinates, in the range 0-1280 and 0-720, respectively.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "touchDraw"
    for coordinate in coordinates:
        command += f" {coordinate:d}"
    result = await client(command)
    return result

async def touchCancel(client: SBBClient) -> str:
    """Cancels current touch operation.

    This method sends the `touchCancel` command to the sys-botbase device and returns the response.

    Args:
        client: An SBBClient object.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "touchCancel"
    result = await client(command)
    return result

"""Keyboard Input"""
async def key(client: SBBClient, *keys: int) -> str:
    """Types several keys on the keyboard in sequence.

    This method sends the `key` command to the sys-botbase device with the given keys and returns the response.

    Args:
        client: An SBBClient object.
        *keys: A list of HidKeyboardKey values.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "key"
    for key in keys:
        command += f" {key:d}"
    result = await client(command)
    return result

async def keyMod(client: SBBClient, *keys: int) -> str:
    """Types several keys on the keyboard in sequence with modifier keys.

    This method sends the `keyMod` command to the sys-botbase device with the given keys and returns the response.

    Args:
        client: An SBBClient object.
        *keys: A list of HidKeyboardKey and HidKeyboardModifier values.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "keyMod"
    for i in range(0, len(keys), 2):
        command += f" {keys[i]:d} {keys[i + 1]:d}"
    result = await client(command)
    return result

async def keyMulti(client: SBBClient, *keys: int) -> str:
    """Presses several keys at the same time.

    This method sends the `keyMulti` command to the sys-botbase device with the given keys and returns the response.

    Args:
        client: An SBBClient object.
        *keys: A list of HidKeyboardKey values.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "keyMulti"
    for key in keys:
        command += f" {key:d}"
    result = await client(command)
    return result

"""Screen Control"""
async def pixelPeek(client: SBBClient) -> str:
    """Returns a .jpg file of the current screen.

    This method sends the `pixelPeek` command to the sys-botbase device and returns the response. The response is the contents of the .jpg file.

    Args:
        client: An SBBClient object.

    Returns:
        The contents of the .jpg file.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "pixelPeek"
    result = await client(command)
    return result

async def screenOff(client: SBBClient) -> str:
    """Turns the screen off.

    This method sends the `screenOff` command to the sys-botbase device and returns the response. The response is a success message.

    Args:
        client: An SBBClient object.

    Returns:
        None.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "screenOff"
    result = await client(command)
    return result

async def screenOn(client: SBBClient) -> str:
    """Turns the screen on.

    This method sends the `screenOn` command to the sys-botbase device and returns the response. The response is a success message.

    Args:
        client: An SBBClient object.

    Returns:
        None.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "screenOn"
    result = await client(command)
    return result

"""Utility"""
async def getTitleID(client: SBBClient) -> str:
    """Returns the title ID of the application currently running.

    This method sends the `getTitleID` command to the sys-botbase device and returns the response. The response is the TitleId of the application currently running.

    Args:
        client: An SBBClient object.

    Returns:
        The title ID of the application currently running.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getTitleID"
    result = await client(command)
    return result

async def getTitleVersion(client: SBBClient) -> str:
    """Returns the version of the title currently running.

    This method sends the `getTitleVersion` command to the sys-botbase device and returns the response. The response is the Version of the Title currently running.

    Args:
        client: An SBBClient object.

    Returns:
        The version of the title currently running.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getTitleVersion"
    result = await client(command)
    return result

async def getSystemLanguage(client: SBBClient) -> str:
    """Returns the language of the Switch OS.

    This method sends the `getSystemLanguage` command to the sys-botbase device and returns the response. The response is the Language of the Switch OS.

    Args:
        client: An SBBClient object.

    Returns:
        The language of the Switch OS.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getSystemLanguage"
    result = await client(command)
    return result

async def getBuildID(client: SBBClient) -> str:
    """Returns the build ID of the Application running.

    This method sends the `getBuildID` command to the sys-botbase device and returns the response. The response is the BuildID of the Application running.

    Args:
        client: An SBBClient object.

    Returns:
        The build ID of the Application running.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getBuildID"
    result = await client(command)
    return result

async def getHeapBase(client: SBBClient) -> str:
    """Returns the memory address of the Heap Base.

    This method sends the `getHeapBase` command to the sys-botbase device and returns the response. The response is the Memory address of the Heap Base.

    Args:
        client: An SBBClient object.

    Returns:
        The memory address of the Heap Base.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getHeapBase"
    result = await client(command)
    return result

async def getMainNsoBase(client: SBBClient) -> str:
    """Returns the memory address of the NSOMain.

    This method sends the `getMainNsoBase` command to the sys-botbase device and returns the response. The response is the Memory address of the NSOMain.

    Args:
        client: An SBBClient object.

    Returns:
        The memory address of the NSOMain.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getMainNsoBase"
    result = await client(command)
    return result

async def isProgramRunning(client: SBBClient, programID: str) -> bool:
    """Checks if program with given id is running.

    This method sends the `isProgramRunning` command to the sys-botbase device with the given programID and returns the response. The response is a boolean value indicating whether the program with the given ID is running.

    Args:
        client: An SBBClient object.
        programID: The ID of the program to check.

    Returns:
        A boolean value indicating whether the program with the given ID is running.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"isProgramRunning {programID}"
    result = await client(command)
    return result

async def game(client: SBBClient, metadata: str) -> str:
    """Returns Metadata about the running game.

    This method sends the `game` command to the sys-botbase device with the given metadata and returns the response. The response is the metadata about the running game, depending on the value of the `metadata` parameter.

    Args:
        client: An SBBClient object.
        metadata: One of the following:
            * `icon`: IconData
            * `version`: Game Version
            * `rating`: Age rating
            * `author`: Author of the game
            * `name`: Name of the game

    Returns:
        The metadata about the running game.

    Raises:
        TimeoutError: If the command times out.
    """
    command = f"game {metadata}"
    result = await client(command)
    return result

async def getVersion(client: SBBClient) -> str:
    """Returns version of sys-botbased used.

    This method sends the `getVersion` command to the sys-botbase device and returns the response. The response is the version of sys-botbased used.

    Args:
        client: An SBBClient object.

    Returns:
        The version of sys-botbased used.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "getVersion"
    result = await client(command)
    return result

async def charge(client: SBBClient) -> str:
    """Returns charge status of the battery.

    This method sends the `charge` command to the sys-botbase device and returns the response. The response is a string indicating the charge status of the battery.

    Args:
        client: An SBBClient object.

    Returns:
        A string indicating the charge status of the battery.

    Raises:
        TimeoutError: If the command times out.
    """
    command = "charge"
    result = await client(command)
    return result

"""Configure"""
async def configure(client: SBBClient, command: str, value: str) -> str:
    """Configures a sys-botbase setting.

    This method sends the `configure` command to the sys-botbase device with the given setting and value and returns the response.

    Args:
        client: An SBBClient object.
        command: The setting to configure.
        value: The new value for the setting.

    Returns:
        The response from the sys-botbase device.

    Raises:
        TimeoutError: If the command times out.
    """

    command = "configure"
    command += f" {command:s} {value:s}"
    result = await client(command)
    return result
