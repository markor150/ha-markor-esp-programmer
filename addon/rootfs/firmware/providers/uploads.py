from pathlib import Path

from firmware.models import FirmwareFile
from firmware.provider import FirmwareProvider


UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class UploadProvider(FirmwareProvider):

    source = "upload"

    def scan(self):
        result = []

        for file in sorted(UPLOAD_DIR.glob("*.bin")):
            result.append(
                FirmwareFile(
                    name=file.name,
                    path=str(file),
                    size=file.stat().st_size,
                    source=self.source,
                ).__dict__
            )

        return result
