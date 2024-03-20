FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
	git gcc tidy python3 python3-pip python3-dev libzmq3-dev curl gnupg \
	libxmlsec1-dev libltdl-dev \
        pkg-config && \
    apt-get clean

#WORKDIR /inginious
RUN pip3 install --no-cache-dir git+https://github.com/jyounggo/INGInious.git@v0.8.7#egg=INGInious[uwsgi,saml2]
