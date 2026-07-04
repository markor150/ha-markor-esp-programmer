ARG BUILD_FROM=ghcr.io/home-assistant/base:3.23
FROM ${BUILD_FROM}

RUN apk add --no-cache \
    python3 \
    py3-pip

COPY rootfs/requirements.txt /requirements.txt

RUN pip3 install --break-system-packages -r /requirements.txt

COPY rootfs/ /

WORKDIR /

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8099"]
