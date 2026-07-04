from pathlib import Path

from firmware.models import FirmwareFile
from firmware.provider import FirmwareProvider


SEARCH_PATHS = [
    Path("/share/markor"),
    Path("/config/esphome"),
    Path("/data/build"),
]


class ESPHomeProvider(FirmwareProvider):
    source = "esphome"

    def scan(self):
        result = []
        seen = set()

        for root in SEARCH_PATHS:
            if not root.exists():
                continue

            for pattern in (
                "*.bin",
                "*.factory.bin",
                "firmware.bin",
                "firmware.factory.bin",
            ):
                for file in root.rglob(pattern):
                    if not file.is_file():
                        continue

                    real = str(file.resolve())

                    if real in seen:
                        continue

                    seen.add(real)

                    result.append(
                        FirmwareFile(
                            name=file.name,
                            path=real,
                            size=file.stat().st_size,
                            source=self.source,
                        ).__dict__
                    )

        return result
