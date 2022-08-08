import pytest_parametrize

@pytest_parametrize.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest_parametrize.mark.xfail
def test_not_succeed():
    assert False


@pytest_parametrize.mark.skip
def test_skipped():
    assert False