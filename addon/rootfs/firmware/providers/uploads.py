from pathlib import Path


UPLOAD_DIR = Path("/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class UploadProvider:
    source = "upload"

    def scan(self):
        result = []

        for file in sorted(UPLOAD_DIR.glob("*.bin")):
            result.append(
                {
                    "name": file.name,
                    "size": file.stat().st_size,
                    "source": self.source,
                    "path": str(file),
                }
            )

        return result
