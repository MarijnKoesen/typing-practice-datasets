# Typing practice datasets

This repo offers a bunch of typing sets that can be used to practice your typing skills.

From different natural languages to programming languages.

It also contains tools to generate more datasets from known, free, sources.


## Contributing

Adding a programming language ideally is done by cloning a few open source repo's and running analysis on them, for
example:

```shell
mkdir go-repos/
git clone --depth=1 https://github.com/golang/go/ go-repos/go
git clone --depth=1 https://github.com/kubernetes/kubernetes go-repos/kubernetes
git clone --depth=1 https://github.com/kubernetes/client-go go-repos/kubernetes-client
git clone --depth=1 https://github.com/spf13/cobra go-repos/cobra
git clone --depth=1 https://github.com/cli/cli go-repos/github-cli
git clone --depth=1 https://github.com/gohugoio/hugo go-repos/hugo
tools/count.py --num=10000 --dont-lowercase --non-alpha --minimum-length=1 go-repos/**/*.go > datasets/programming/golang.top.10000.txt
```
