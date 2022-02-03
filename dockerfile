FROM python:latest
LABEL org.opencontainers.image.authors="kaan.gure@mail.mcgill.ca"

WORKDIR /usr/app/src

COPY send_receive.py ./

CMD ["python", "./send_receive.py"]