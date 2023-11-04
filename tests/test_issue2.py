import sys
import os
import pytest
sys.path.append(os.getcwd())
from morse import decode


@pytest.mark.parametrize("morse_message, expected", [
    ('... --- ...', 'SOS'),
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('.- ...- .. - ---', 'AVITO'),
    ('.---- ..--- ...--', '123'),
    ('.... . .-.. .-.. ---   .-- --- .-. .-.. -..', 'HELLO WORLD')])
def test_decode(morse_message, expected):
    assert decode(morse_message) == expected
