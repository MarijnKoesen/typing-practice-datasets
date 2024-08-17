# Different tools to generate word lists

* [How to create word lists from any file collection](#Count.py)
* [How to generate natural language lists from Project Gutenberg](#Count.py)

## Count.py

Script to parse files and count the tokens/words:

```shell
usage: count.py [-h] [-n NUM] [-v] [--minimum-length MINIMUM_LENGTH] [--maximum-length MAXIMUM_LENGTH] [--non-alpha] [--words | --trigrams] files [files ...]

positional arguments:
  files                 <Required> Files to count contents of

options:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     Amount to output
  -v, --verbose         Verbose output
  --minimum-length MINIMUM_LENGTH
                        Minimum word length
  --maximum-length MAXIMUM_LENGTH
                        Maxmimum word length
  --non-alpha           Include non-alpha numeric tokens
  --words               Count words
  --trigrams            Count trigrams
```

### Examples

Count the most used words:
```shell
$ count.py -n 10 books/*.txt
12669 the
8041 and
6150 of
5325 to
3711 in
2714 that
2631 it
2574 was
2216 is
1779 he
```

Filter out short words
```shell
$ count.py -n 5 --minimum-length=4 books/*.txt
2714 that
1735 with
1130 this
1047 they
1011 have
```

Raw output
```shell
$ count.py --raw --num=5 --minimum-length=4 books/*.txt
that with this they have
```

Count trigrams 
```shell
$ count.py --raw --num=20 --trigrams books/*.txt
the and ing hat her tha ere was his for ith thi not ent wit ver all ter you but
```

Include non-alpha numeric words (e.g. for programming languages):
```shell
$ count.py --num=10 --non-alpha --minimum-length=1 go-src/**/*.go
365715 //
334955 =
323947 {
308374 }
188615 :=
159601 if
150792 the
117446 return
85739 func
80924 !=
```


