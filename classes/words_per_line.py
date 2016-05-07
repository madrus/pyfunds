from urllib.request import urlopen


def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


def analyse(file_name):
    """Count the number of words per line in a local text file
    with a given name.
    E.g.:
        analyse('wasteland.txt')

    Args:
        file_name: A local file name
    """
    with open(file_name, mode='rt', encoding='utf-8') as flo:
        return words_per_line(flo)


def webanalyse(file_name):
    """Count the number of words per line in a remote text file
    with a given name.
    E.g.:
        webanalyse('http://sixty-north.com/c/t.txt')

    Args:
        file_name: A remote file name
    """
    with urlopen(file_name) as flo:
        return words_per_line(flo)

