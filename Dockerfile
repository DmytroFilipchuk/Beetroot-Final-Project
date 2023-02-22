FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /Beetroot-Final-Project

COPY . /Beetroot-Final-Project

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg
RUN apt-get install -y python3.10

CMD ["python3.10", "app.py"]

