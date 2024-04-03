from pathlib import Path
from setuptools import setup

# This is where you add any fancy path resolution to the local lib:
local_path: str = (Path(__file__).parent.parent / "namespace-utils").as_uri()

setup(
    install_requires=[
        "aiohttp>=3.8.3,<4.0.0",
        f"namespace-utils @ {local_path}",
    ]
)