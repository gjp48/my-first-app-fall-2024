# this is the "test/rps_test.py" file...

from app.rps import determine_outcome


def test_example():
    assert 2 + 2 == 4

def test_winners():
    # tests for all edge cases:

    assert determine_outcome(u="rock", c="rock") == "TIE GAME"
    assert determine_outcome(u="rock", c="paper") == "COMPUTER WINS"
    assert determine_outcome(u="rock", c="scissors") == "USER WINS"

    assert determine_outcome(u="paper", c="rock") == "USER WINS"
    assert determine_outcome(u="paper", c="paper") == "TIE GAME"
    assert determine_outcome(u="paper", c="scissors") == "COMPUTER WINS"

    assert determine_outcome(u="scissors", c="scissors") == "TIE GAME"
    assert determine_outcome(u="scissors", c="paper") == "USER WINS"
    assert determine_outcome(u="scissors", c="rock") == "COMPUTER WINS"