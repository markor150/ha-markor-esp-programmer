ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base-python:3.13

FROM ${BUILD_FROM}

RUN pip install esptool fastapi uvicorn

COPY rootfs /

CMD ["python3","/app.py"]
