import pytest

rerun_trigger = 0

@pytest.mark.phase_1_2
def test_to_be_rerun():
    global rerun_trigger
    if rerun_trigger == 0:
        rerun_trigger = 1
        assert False, "expected failure to check rerun trigger"
    assert True, "test field after second attempt"
