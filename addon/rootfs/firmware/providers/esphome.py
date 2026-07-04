from pathlib import Path

from firmware.models import FirmwareFile
from firmware.provider import FirmwareProvider


SEARCH_PATHS = [
    "/share/markor",
    "/config/esphome",
    "/data/build",
]


class ESPHomeProvider(FirmwareProvider):

    source = "esphome"

    def scan(self):
        result = []
        seen = set()

        for root_name in SEARCH_PATHS:
            root = Path(root_name)

            if not root.exists():
                print(f"[ESPHome] Missing: {root}")
                continue

            print(f"[ESPHome] Scanning: {root}")

            for file in root.rglob("*.bin"):

                if not file.is_file():
                    continue

                real = str(file.resolve())

                if real in seen:
                    continue

                seen.add(real)

                print(f"[ESPHome] Found: {real}")

                result.append(
                    FirmwareFile(
                        name=file.name,
                        path=real,
                        size=file.stat().st_size,
                        source=self.source,
                    ).__dict__
                )

        print(f"[ESPHome] Total firmware: {len(result)}")

        return result
