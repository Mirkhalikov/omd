from morse import encode
import sys
import os
sys.path.append(os.getcwd())


def test_encode():
    """
    >>> encode("SOS")
    '... --- ...'
    >>> encode("HELLO WORLD")
    '.... . .-.. .-.. ---   .-- --- .-. .-.. -..'
    >>> encode("123")
    '.---- ..--- ...--'
    >>> encode("")
    ''
    >>> encode("!")
    Traceback (most recent call last):
        ...
    KeyError: '!'

    >>> encode("HELLO, WORLD")
    Traceback (most recent call last):
        ...
    KeyError: ','
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
