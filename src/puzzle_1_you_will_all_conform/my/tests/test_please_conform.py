import random
from typing import List, Set
from unittest import TestCase

from please_conform import PleaseConform
from please_conform_squared import PleaseConformSquared
from structures import Interval


class TestPleaseConform(TestCase):
    def setUp(self) -> None:
        self.caps: Set[str] = set()
        self.caps.add('F')
        self.caps.add('B')

        self.solution: PleaseConform = self.get_solution()

    def get_solution(self) -> PleaseConform:
        return PleaseConformSquared()

    def get_random_number(self) -> int:
        return random.randrange(1, 42)

    def test_empty(self):
        caps: List[str] = list()

        result_expected = list()

        result_actual = self.solution.please_conform(caps)

        self.assertEqual(result_expected, result_actual)

    def test_single(self):
        for cap in self.caps:
            caps: List[str] = [cap for _ in range(self.get_random_number())]

            result_expected = list()

            result_actual = self.solution.please_conform(caps)

            self.assertEqual(result_expected, result_actual)

    def test_middle(self):
        print(len(self.caps))
        border_cap: str = self.caps.pop()
        middle_cap: str = self.caps.pop()

        border_count_left: int = self.get_random_number()
        border_count_right: int = self.get_random_number()
        middle_count: int = self.get_random_number()

        caps: List[str] = list()
        caps += [border_cap for _ in range(border_count_left)]
        caps += [middle_cap for _ in range(middle_count)]
        caps += [border_cap for _ in range(border_count_right)]

        result_expected: List[Interval] = [Interval(start=border_count_left,
                                                    end=border_count_left + middle_count - 1,
                                                    cap_type=middle_cap)]

        result_actual = self.solution.please_conform(caps)

        self.assertEqual(result_expected, result_actual)
