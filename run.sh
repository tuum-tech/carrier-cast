#!/bin/bash

docker container stop carrier-cast || true && docker container rm -f carrier-cast || true

docker run -d                                   \
    --sysctl fs.mqueue.msg_max=50               \
    --name carrier-cast                         \
    -v "$PWD/.carrier-logs:/root/.carrier"      \
    -p 5000:5000                                \
    tuumtech/carrier-cast:latest