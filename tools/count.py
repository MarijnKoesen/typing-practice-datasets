#!/usr/bin/env python3
import argparse, sys
from collections import Counter
import collections
import glob

parser=argparse.ArgumentParser()
parser.add_argument("-n", "--num", help="Amount to output", default=1000, type=int)
parser.add_argument("-v", "--verbose", action='store_true', help="Verbose output")
parser.add_argument("-r", "--raw", action='store_true', help="Output words only")
parser.add_argument("--dont-lowercase", help="Don't lowercase words", action='store_true', default=False)
parser.add_argument("--minimum-length", help="Minimum word length", type=int, default=2)
parser.add_argument("--maximum-length", help="Maxmimum word length", type=int, default=99)
parser.add_argument("--non-alpha", action='store_true', help="Include non-alpha numeric tokens", default=False)
modeGroup = parser.add_mutually_exclusive_group()
modeGroup.add_argument("--words", action='store_true', help="Count words")
modeGroup.add_argument("--trigrams", action='store_true', help="Count trigrams")
parser.add_argument("files", help='<Required> Files to count contents of', nargs="+")
args=parser.parse_args()

words = Counter([])

for f in args.files:
    for file in glob.glob(f, recursive=True):
        if args.verbose:
            print("Processing: " + file, file=sys.stderr)

        try:
            wordsInFile = open(file, "r").read().split() or []
        except IsADirectoryError:
            continue

        words.update(
            map(
                lambda word: word if args.no_lower else word.lower(),
                filter(
                    lambda word: (args.non_alpha == True or word.isalpha()) and len(word) >= args.minimum_length and len(word) <= args.maximum_length,
                    wordsInFile
                )
            )
        )

if args.trigrams:
    trigrams = {}
    for word, count in words.items():
        for start in range(0, len(word) - 2):
            trigram = word[start:start+3].lower()
            # print("   " + trigram)

            if not trigram.isalpha():
                continue

            if trigram not in trigrams:
                trigrams[trigram] = 0

            trigrams[trigram] += count

    od = collections.OrderedDict(sorted(trigrams.items(), key = lambda x:(-x[1],x[0])))
    for word, count in list(od.items())[0:args.num]:
        if args.raw:
            print(word, end=" ")
        else:
            print(count, word)
else:
    for word, count in words.most_common(args.num):
        if args.raw:
            print(word, end=" ")
        else:
            print(count, word)

