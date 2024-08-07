#!/bin/bash
VERSION=v0.8
NO_CACHE=1
if [ $NO_CACHE -eq 1 ]; then
   docker build --no-cache -t csr.csel.io/inginious/inginious:${VERSION} .
else
   docker build -t csr.csel.io/inginious/inginious:${VERSION} .
fi
