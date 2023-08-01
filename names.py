"""
Utility functions for working with MusicBrainz or Last.fm strings
understood as names or titles.
"""

import jellyfish

SINGLE_QUOTES = '\u2018\u2019\u201a\u201b'
DOUBLE_QUOTES = '\u201c\u201d\u201e\u201f\u2033'
DASHES = '\u2010\u2012\u2013\u2014\u2015'
PUNCTUATION = '\u2026'


def is_untitled(name):
    """
    Check if the argument string matches any of the "untitled"
    patterns. The comparison is case insensitive.
    """
    untitled_patterns = ['[untitled]', 'untitled']

    return name.casefold() in untitled_patterns


def asciify(name):
    """
    Return a new string where the typographically correct single
    quotes, double quotes, dashes and punctuation are changed to
    their plain ASCII counterparts.
    """
    if not is_typographic(name):
        return name

    typographic = SINGLE_QUOTES + DOUBLE_QUOTES + DASHES
    plain_ascii = '\'' * len(SINGLE_QUOTES) + '"' * len(DOUBLE_QUOTES) + '-' * len(DASHES)
    mapper = str.maketrans(typographic, plain_ascii)

    return name.translate(mapper).replace('\u2026', '...')


def normalize(name):
    """
    Return a new string where the typographically correct characters
    are changed to plain ASCII counterparts. The string is converted
    to lower case.
    """
    return asciify(name).casefold()


def cmp_normalized(name, other_name):
    """Compare two normalized names."""
    if not is_typographic(name) and not is_typographic(other_name):
        return name.casefold() == other_name.casefold()

    return normalize(name) == normalize(other_name)


def is_typographic(name):
    """
    Check if the argument string contains typographically correct,
    non-ASCII single quotes, double quotes, dashes or punctuation.
    """
    typographic_chars = SINGLE_QUOTES + DOUBLE_QUOTES + DASHES + PUNCTUATION

    for char in name:
        if char in typographic_chars:
            return True

    return False


def replace_numbers(name, repeat=10):
    """
    Return a new string where all embedded numbers are replaced with
    fixed long sequences of letters which differ from one another in
    terms of fuzzy string matching. The purpose of this is to increase
    the edit distance between track titles that differ only by numbers,
    such as "Song Title, Part N".
    TODO: handle Roman numerals
    """
    replace = {
        '0': 'y' * repeat,
        '1': 'p' * repeat,
        '2': 'j' * repeat,
        '3': 'x' * repeat,
        '4': 'b' * repeat,
        '5': 'z' * repeat,
        '6': 'k' * repeat,
        '7': 'q' * repeat,
        '8': 'v' * repeat,
        '9': 'g' * repeat
    }

    for key, val in replace.items():
        name = name.replace(key, val)
    return name


def cmp_fuzzy_normalized_numbers(name, other_name):
    """
    Compare two strings using fuzzy algorithm. Both input strings are
    converted to lower case, typographic characters are changed to ASCII
    counterparts, and numbers are replaced with fixed letter sequences to
    increase edit distance between strings which only differ by digits.
    """
    cmp_name = replace_numbers(normalize(name))
    cmp_other_name = replace_numbers(normalize(other_name))

    return jellyfish.jaro_winkler(cmp_name, cmp_other_name)
