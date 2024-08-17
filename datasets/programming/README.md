## Contributing

Adding a programming language ideally is done by cloning a few open source repo's with the MIT license and running 
analysis on them, for example:

```shell
cd typing-practice-datasets

mkdir sources/go-repos/
git clone --depth=1 https://github.com/ollama/ollama sources/golang/ollama
git clone --depth=1 https://github.com/gin-gonic/gin sources/golang/gin
git clone --depth=1 https://github.com/junegunn/fzf sources/golang/fzf
git clone --depth=1 https://github.com/nektos/act sources/golang/act
git clone --depth=1 https://github.com/traefik/traefik sources/golang/traefik
git clone --depth=1 https://github.com/jesseduffield/lazygit sources/golang/lazygit

mkdir datasets/programming/golang/
tools/count.py --num=10000 --dont-lowercase --non-alpha --minimum-length=1 'sources/golang/**/*.go' > datasets/programming/golang/golang.top.10000.txt
cat datasets/programming/golang/golang.top.10000.txt | awk '{ print $1 }' > datasets/programming/golang/golang.top.10000.raw.txt
head -n 1000 datasets/programming/golang/golang.top.10000.txt > datasets/programming/golang/golang.top.1000.txt
head -n 1000 datasets/programming/golang/golang.top.10000.raw.txt > datasets/programming/golang/golang.top.1000.raw.txt
```

NOTE: Please use MIT projects only to prevent any licensing issues.

You can find the most popular projects here: https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Go.md

## Using your own (private) project to train yourself

Of/c you can use this project to generate some typing practice for your own (potentially private) repos. 

It's a great way to practice your skills on something that's close to what you are working with.