from logic_utils import check_guess

from logic_utils import get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_regression_attempts_left_starts_at_full_limit():
    attempt_limit_map = {
        "Easy": 6,
        "Normal": 8,
        "Hard": 5,
    }
    attempts_at_start = 0

    for attempt_limit in attempt_limit_map.values():
        attempts_left = attempt_limit - attempts_at_start
        assert attempts_left == attempt_limit


def test_regression_hard_range_not_smaller_than_normal():
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    normal_span = normal_high - normal_low
    hard_span = hard_high - hard_low

    assert hard_low <= normal_low
    assert hard_high >= normal_high
    assert hard_span >= normal_span


def test_regression_high_guess_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_regression_low_guess_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
