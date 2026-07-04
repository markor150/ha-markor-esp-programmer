ARG BUILD_FROM=ghcr.io/home-assistant/base:3.23
FROM ${BUILD_FROM}

RUN apk add --no-cache \
    python3 \
    py3-pip

RUN pip3 install --break-system-packages \
    esptool \
    fastapi \
    uvicorn \
    python-multipart

COPY rootfs/requirements.txt /requirements.txt
RUN pip3 install --break-system-packages -r /requirements.txt

COPY rootfs /

