FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PKG_DIR /tmp/pkg
ENV SRC_DIR /opt

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
RUN apt-get update
RUN apt-get install -y g++ default-jdk

# install mecab
RUN apt-get install -y curl git
RUN curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | /bin/bash

COPY requirements.txt ${PKG_DIR}/requirements.txt

RUN pip install --upgrade pip && \
    pip install --upgrade -r ${PKG_DIR}/requirements.txt

RUN rm -rf /tmp/*
ARG CACHEBUST=1
COPY src ${SRC_DIR}
WORKDIR ${SRC_DIR}

ENV PORT 50051
EXPOSE ${PORT}
ENV PYTHONPATH "${PYTONPATH}:${SRC_DIR}"

ENTRYPOINT ["homi"]
CMD ["run","konlpy_homi/app.py","-w","100","-p","50051"]
