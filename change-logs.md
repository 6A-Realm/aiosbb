# Change Log

All notable changes to this project will be documented in this file.

## 0.1.1 (2023-09-27)

### Added

- Docstrings to help document code.
- Added Dunder variables.
- New `disconnect` method to `SBBClient` class to add ability to disconnect from sys-botbase device.
    ```py
    # Creating a connection to device.
    client = SBBClient("192.168.1.2")

    # Terminating connection to device.
    await client.disconnect()
    ```
- When debug is selected, `printDebugResultCodes` is added to the init_commands.

### Changed

- Context manager used to ensure that setattr() call is always executed, even if an exception occurs.
- sys-botbase may be rebuilt to be used with a different port. The option to change port was added.
- Logging messages was reformatted.

### Fixed

- None

