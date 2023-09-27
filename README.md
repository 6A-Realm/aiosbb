# aiosbb
Asynchronous sys-botbase client/server framework in Python.

## Installation
Python 3.8 or higher is required

Run the following command to install the library:
```
# Linux/macOS
python3 -m pip install -U aiosbb

# Windows
py -3 -m pip install -U aiosbb
```

## Examples
Examples utilizing this package.

### Quick Example
```py
from asyncio import run
from aiosbb import SBBClient


HOST = "192.168.1.2"

async def main() -> None:
    """Run the SBBClient."""
    client = SBBClient(HOST)

    """Send and recieve bytes from the sys-botbase device."""
    title_id = await client("getTitleID")
    print(title_id)


if __name__ == "__main__":
    run(main())
```

### Reformatted Into Class
```py
import asyncio
from aiosbb import SBBClient


class SBBDevice:
    def __init__(self, host: str):
        self.client = SBBClient(host)

    async def get_title_id(self) -> str:
        """Get the title ID of the sys-botbase device."""
        return await self.client("getTitleID")


async def main():
    """Run the SBBDevice."""
    device = SBBDevice(HOST)

    title_id = await device.get_title_id()
    print(title_id)


if __name__ == "__main__":
    asyncio.run(main())
```

## Usage
Once an instance of the `SBBClient` class, you can call the `client()` method which takes the name of the command as an argument. For example, to send the `press A` command, you would call the method as follows:
```py
select = await client("press A")
```

The full list of supported [sys-botbase](https://github.com/olliz0r/sys-botbase/tree/master) commands can be [found here](https://github.com/olliz0r/sys-botbase/blob/master/commands.md).