FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
	git gcc tidy python3 python3-pip python3-dev libzmq3-dev curl gnupg vim-tiny \
        libxml2 libxmlsec1 \
	libltdl-dev \
        pkg-config && \
    apt-get clean

# Fix uwsgi crash on startup : Do not install libxml2-dev
RUN apt-get remove -y libxml2-dev

# Create a user
RUN useradd -r -u 1000 inginious
RUN pip3 install --no-cache-dir git+https://github.com/jyounggo/INGInious.git@inginious-0.8#egg=INGInious[uwsgi,saml2]
WORKDIR /inginious
