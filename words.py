#! python3
"""Retrieve and print words from a URL using Python3.

Usage:

    python words.py <URL>
"""

import sys
from urllib.request import urlopen

"""
We have styled this modules with docstrings
according to the Google Documents Style Guide)

URL = 'http://sixty-north.com/c/t.txt'
"""

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: the URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words
        from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            # line_words = line.split()
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Print items one per line.

    Args:
        items: an iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL.

    Args:
        url: the URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


"""
__name__ is a special variable, its value depends on how it is being used
1. if called from REPL, it shows the module's name but only once, the very first time
2. if called via console, it returns '__main__' as a string
This allows us to test how the module is called
"""
# print(__name__)


# this will only work if called via console and not from REPL
if __name__ == '__main__':
    main(sys.argv[1]) # The 0th arg is the module filename
