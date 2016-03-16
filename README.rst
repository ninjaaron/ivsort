ivsort.py
=========

a simple script to sort Hebrew words with vowels and accents according
to their lexical order (which differs from the unicode point order or
even the locale's collation string)

From the docstring:

    Module for properly sorting Hebrew words with niqqud -- according to
    consonants first and vowels later. If run from the command line, takes a
    file with a list of words as input or reads lines from stdin.

    disclaimer: there is no universal method for the ordering of Hebrew
    vowels. The order used by this module is:

      Sheva, Hataf Segol, Hataf Patah, Hataf Qamets,
      Hiriq, Tsere, Segol, Patah, Qamets, Holem, Holem Vav, Qibbuts, Shureq

    This order may seem foreign to those accustomed to Latin-based
    languages, but it was recommended to me by the Academy for the Hebrew
    Language in Israel, and it is very similar to orders use by Unicode and
    standard Israeli keyboard layouts. It is also more "scientific" in the
    sense that it follows a phonological pattern (horizontal to vertical
    vowels), rather than a traditional, Latin-based pattern (aeiou).

    This does differ from the one convention common in Israeli works, in
    that it treats Sin as a separate letter from Shin. This is not
    especially common in Israel, but it is the convention in all of the
    widely used Biblical lexicons and other Western Biblical scholarship. I
    do this both because it would be pedagogical malpractice to give my
    students glossaries that differ in this regard from the works they will
    be using later, and because it is more accurate from the perspective of
    historical linguistics.

    I would probably revise this approach if this sort engine were targeted
    at modern Hebrew.


Usage
-----

At the command line::
    $ cat wordlist.txt | ivsort.py
    ...
    $ ivsort.py wordlist.txt

So it can read from a file or from STDIN, so as to be useful for text
editors that can use shell commands as filters (like all of them that
matter). It is basically how `sort` works.

As a Python3 module::
    from ivsort import ivsort
    sorted_list = ivsort(unsorted_iterable)

You probably aren't going to want to muck around with the other
functions this script provides.
