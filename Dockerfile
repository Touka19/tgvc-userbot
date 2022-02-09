FROM python:3.9.1-buster

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel

COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt

WORKDIR /tgvc-userbot-dev
COPY x.sh /x.sh

CMD ["bash", "/x.sh"]
