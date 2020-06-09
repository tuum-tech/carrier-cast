#!/bin/bash

docker container stop carrier-cast || true && docker container rm -f carrier-cast || true

docker run -it --name carrier-cast \
    -p 5000:5000 \
    tuum-tech/carrier-cast:latest