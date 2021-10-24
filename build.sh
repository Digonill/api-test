#! /bin/bash

docker image rm -f api-test

docker build . -t api-test