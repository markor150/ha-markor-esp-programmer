ARG BUILD_FROM
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --break-system-packages \
    esptool \
    fastapi \
    uvicorn

COPY rootfs /

CMD ["python3","/app.py"]
