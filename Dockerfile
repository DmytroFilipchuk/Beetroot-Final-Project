FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y ffmpeg
RUN apt-get install -y python3.10
ENTRYPOINT ["python3"]