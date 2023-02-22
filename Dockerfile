FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /Beetroot-Final-Project

COPY . /Beetroot-Final-Project

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg

CMD ["python3", "app.py"]

