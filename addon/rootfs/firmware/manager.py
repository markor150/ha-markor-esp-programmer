from firmware.providers.uploads import UploadProvider


class FirmwareManager:
    def __init__(self):
        self.providers = [
            UploadProvider(),
        ]

    def scan(self):
        result = []

        for provider in self.providers:
            result.extend(provider.scan())

        return sorted(
            result,
            key=lambda x: (
                x["source"],
                x["name"].lower(),
            ),
        )
