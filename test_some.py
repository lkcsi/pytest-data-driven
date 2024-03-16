import pytest


@pytest.mark.data_driven
def test_dd_2(field_1, field_2, field_3, field_4):
    assert field_1 > 0


@pytest.mark.data_driven
def test_some_other(field_1, field_2):
    assert field_1 > field_2


def test_ordinary():
    assert 1 == 1
