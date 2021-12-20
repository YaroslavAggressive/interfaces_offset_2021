from typing import List

import pytest

from kvest_task import check_keys


class Case:
    def __init__(self, name: str,
                 keys_num: int, links: List[List[int]],
                 links_for_check: List[List[int]], answer: List[bool]):
        self._name = name
        self.keys_num = keys_num
        self.links = links
        self.links_for_check = links_for_check
        self.answer = answer

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        keys_num=4,
        links=[[1, 2], [1, 0], [2, 0], [2, 3]],
        links_for_check=[[1, 0], [1, 2], [3, 2]],
        answer=[True, True, False]
    ),
    Case(
        name='base2',
        keys_num=3,
        links=[[1, 2], [1, 0], [2, 0]],
        links_for_check=[[1, 0], [1, 2]],
        answer=[True, True]
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = check_keys(
        keys_num=case.keys_num,
        links=case.links,
        links_for_check=case.links_for_check
    )
    assert answer == case.answer