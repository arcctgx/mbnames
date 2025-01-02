"""String comparison and related functions."""

from jellyfish import jaro_winkler_similarity

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


def cmp_fuzzy(name: str, other_name: str) -> float:
    """
    Compare two strings using a fuzzy matching algorithm. Return a floating
    point value between 0.0 and 1.0, where 0.0 indicates no similarity and
    1.0 indicates an exact match.

    This is a thin wrapper around a function provided by a third-party library.
    The idea is to have only one place which references a third-party function.
    This will make it easy to consistently change the fuzzy comparison method
    across the code.
    """
    return jaro_winkler_similarity(name, other_name)


def cmp_normalized_fuzzy(name: str, other_name: str) -> float:
    """
    Compare two strings using fuzzy algorithm. Both input strings are
    converted to lower case, typographic characters are changed to ASCII
    counterparts, and numbers are replaced with fixed letter sequences to
    increase edit distance between strings which only differ by digits.
    """
    cmp_name = replace_numbers(normalize(name))
    cmp_other_name = replace_numbers(normalize(other_name))

    return cmp_fuzzy(cmp_name, cmp_other_name)
