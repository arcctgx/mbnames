"""String comparison and related functions."""

import jellyfish

from mbnames.names import is_typographic, normalize


def replace_numbers(name: str, repeat: int = 10) -> str:
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


def cmp_normalized(name: str, other_name: str) -> bool:
    """Compare two normalized names."""
    if not is_typographic(name) and not is_typographic(other_name):
        return name.casefold() == other_name.casefold()

    return normalize(name) == normalize(other_name)


def cmp_normalized_fuzzy(name: str, other_name: str) -> float:
    """
    Compare two strings using fuzzy algorithm. Both input strings are
    converted to lower case, typographic characters are changed to ASCII
    counterparts, and numbers are replaced with fixed letter sequences to
    increase edit distance between strings which only differ by digits.
    """
    cmp_name = replace_numbers(normalize(name))
    cmp_other_name = replace_numbers(normalize(other_name))

    return jellyfish.jaro_winkler_similarity(cmp_name, cmp_other_name)
