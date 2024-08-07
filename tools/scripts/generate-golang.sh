#!/usr/bin/env bash

cd $(dirname $0)

mkdir /tmp/go-repos/
git clone --depth=1 https://github.com/golang/go/ /tmp/go-repos/go
git clone --depth=1 https://github.com/kubernetes/kubernetes /tmp/go-repos/kubernetes
git clone --depth=1 https://github.com/kubernetes/client-go /tmp/go-repos/kubernetes-client
git clone --depth=1 https://github.com/spf13/cobra /tmp/go-repos/cobra
git clone --depth=1 https://github.com/cli/cli /tmp/go-repos/github-cli
git clone --depth=1 https://github.com/gohugoio/hugo /tmp/go-repos/hugo
../count.py -v --num=10000 --no-lower --non-alpha --minimum-length=1 '/tmp/go-repos/**/*.go' > ../../datasets/programming/golang.top.10000.txt