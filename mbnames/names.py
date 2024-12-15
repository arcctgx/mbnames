"""
Utility functions for working with MusicBrainz or Last.fm artist credit
and title strings.
"""

from typing import Optional

_SINGLE_QUOTES = '\u2018\u2019\u201a\u201b'
_DOUBLE_QUOTES = '\u201c\u201d\u201e\u201f\u2033'
_DASHES = '\u2010\u2012\u2013\u2014\u2015'
_PUNCTUATION = '\u2026'


def is_untitled(name: str) -> bool:
    """
    Check if the argument string matches any of the "untitled"
    patterns. The comparison is case insensitive.
    """
    untitled_patterns = ['[untitled]', 'untitled']

    return name.casefold() in untitled_patterns


def asciify(name: str) -> str:
    """
    Return a new string where the typographically correct single
    quotes, double quotes, dashes and punctuation are changed to
    their plain ASCII counterparts.
    """
    if not is_typographic(name):
        return name

    typographic = _SINGLE_QUOTES + _DOUBLE_QUOTES + _DASHES
    plain_ascii = '\'' * len(_SINGLE_QUOTES) + '"' * len(_DOUBLE_QUOTES) + '-' * len(_DASHES)
    mapper = str.maketrans(typographic, plain_ascii)

    return name.translate(mapper).replace('\u2026', '...')


def normalize(name: str) -> str:
    """
    Return a new string where the typographically correct characters
    are changed to plain ASCII counterparts. The string is converted
    to lower case.
    """
    return asciify(name).casefold()


def is_typographic(name: str) -> bool:
    """
    Check if the argument string contains typographically correct,
    non-ASCII single quotes, double quotes, dashes or punctuation.
    """
    typographic_chars = _SINGLE_QUOTES + _DOUBLE_QUOTES + _DASHES + _PUNCTUATION

    for char in name:
        if char in typographic_chars:
            return True

    return False


def remove_featured(name: str, feat_string: Optional[str]) -> str:
    """
    Discard the part of name after the first occurrence of feat_string,
    including feat_string.
    """
    if feat_string is None or not feat_string:
        return name

    pos = name.find(feat_string)
    if pos == -1:
        return name

    return name[:pos].rstrip()
