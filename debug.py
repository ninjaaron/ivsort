#!/usr/bin/env python3

import sys
import six
import ivsort


def main():
    """print the output of a sort"""
    import sys
    try:
        wordlist = open(sys.argv[1])
    except IndexError:
        wordlist = sys.stdin
    if six.PY2:
        wordlist = [w.decode('UTF-8') for w in wordlist]
    for word in sorted(wordlist, key=ivsort.sortkey):
        word = word.rstrip()
        print(word)
        print('  '.join(char for char in word))
        print('  '.join(char for char in ivsort.substitutions(word)
                        if char in ivsort.ORDER2))
        print(ivsort.sortkey(word))


if __name__ == "__main__":
    main()
