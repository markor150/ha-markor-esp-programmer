from dataclasses import dataclass


@dataclass
class FirmwareFile:
    name: str
    path: str
    size: int
    source: str
    chip: str = ""
    version: str = ""
    created: str = ""
