# from src.pre_built.counter import count_ocurrences
# import json
# import pytest
from src.pre_built.counter import count_ocurrences


# @pytest.fixture
def test_counter():
    assert count_ocurrences('data/jobs.csv', 'industry') == 1346
