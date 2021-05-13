"""
Utility functions for working with MusicBrainz or Last.fm strings
understood as names or titles.
"""

SINGLE_QUOTES = '\u2018\u2019\u201a\u201b'
DOUBLE_QUOTES = '\u201c\u201d\u201e\u201f'
DASHES = '\u2012\u2013\u2014\u2015'
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
    single_quotes_tab = str.maketrans(SINGLE_QUOTES, '\''*len(SINGLE_QUOTES))
    double_quotes_tab = str.maketrans(DOUBLE_QUOTES, '"'*len(DOUBLE_QUOTES))
    dashes_tab = str.maketrans(DASHES, '-'*len(DASHES))

    plain = name.translate(single_quotes_tab) \
                .translate(double_quotes_tab) \
                .translate(dashes_tab) \
                .replace('\u2026', '...')

    return plain

def normalize(name):
    """
    Return a new string where the typographically correct characters
    are changed to plain ASCII counterparts. The string is converted
    to lower case.
    """
    return asciify(name).casefold()

def cmp_normalized(name, other_name):
    """Compare two normalized names."""
    return normalize(name) == normalize(other_name)

def is_typographic(name):
    """
    Check if the argument string contains typographically correct,
    non-ASCII single quotes, double quotes, dashes or punctuation.
    """
    typographic_chars = SINGLE_QUOTES + DOUBLE_QUOTES + DASHES + PUNCTUATION

    for char in typographic_chars:
        if char in name:
            return True

    return False
