## Datasets to practice the most common words of a language

These datasets are based on the freely available books from [Project Gutenberg](https://www.gutenberg.org/).

Using the provided tools it's easy to generate a training set.

### Adding a new language

1) First download the`.zim` archive with all the Gutenberg books for your wanted language: https://download.kiwix.org/zim/gutenberg/

2) Next convert all the books into the text format:

```shell
cd typing-practice-datasets/
docker build -t typing-practice-datasets:latest .

mkdir -p sources/gutenberg-texts-en/
docker run \
  --rm \
  -v $PWD/sources/gutenberg-texts-en:/dest \
  -v $PWD/gutenberg_en_all_2023-08.zim:/gutenberg-archive.zim \
  typing-practice-datasets:latest \
  process-gutenberg /gutenberg-archive.zim /dest/
```

3) Check the contents of the `sources/gutenberg-texts-en/` folder, you will find all the books extracted as `txt` here.

4) Use the `tools/count.py` script to create the statistics, for example:

```shell
$ mkdir datasets/languages/english2/
$ tools/count.py -n 10000 'sources/gutenberg-texts-en/*.txt' > datasets/languages/english2/words.top10000.txt
$ tools/count.py -n 1000 --trigrams 'sources/gutenberg-texts-en/*.txt' > datasets/languages/english2/trigrams.top1000.txt
```

5) Use this simple script to generate the other smaller and raw datasets:

```shell
cd datasets/languages/english/
cat trigrams.top1000.txt | awk '{ print $1 }' > trigrams.top1000.raw.txt
head -n 100 trigrams.top1000.txt > trigrams.top100.txt
head -n 100 trigrams.top1000.raw.txt > trigrams.top100.raw.txt

cat words.top10000.txt | awk '{ print $1 }' > words.top10000.raw.txt
head -n 1000 words.top10000.txt > words.top1000.txt
head -n 1000 words.top10000.raw.txt > words.top1000.raw.txt
```