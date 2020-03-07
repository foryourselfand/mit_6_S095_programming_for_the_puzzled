import random
from typing import List, Set
from unittest import TestCase

from please_conform import PleaseConform
from please_conform_linear import PleaseConformLinear
from please_conform_squared import PleaseConformSquared
from structures import Interval


class TestPleaseConform(TestCase):
    def setUp(self) -> None:
        self.solutions: List[PleaseConform] = list()
        self.solutions.append(PleaseConformSquared())
        self.solutions.append(PleaseConformLinear())

        self.caps: Set[str] = set()
        self.caps.add('F')
        self.caps.add('B')

    def test_empty(self):
        caps: List[str] = list()

        expected_result = list()

        for solution in self.solutions:
            actual_result = solution.please_conform(caps)

            self.assertEqual(expected_result, actual_result)

    def test_single(self):
        for cap in self.caps:
            caps: List[str] = [cap for _ in range(random.randrange(1, 42))]

            expected_result = list()

            for solution in self.solutions:
                actual_result = solution.please_conform(caps)

                self.assertEqual(expected_result, actual_result)

    def test_middle(self):
        border_cap: str = self.caps.pop()
        middle_cap: str = self.caps.pop()

        caps: List[str] = list()
        caps += [border_cap for _ in range(3)]
        caps += [middle_cap for _ in range(1)]
        caps += [border_cap for _ in range(3)]

        expected_result: List[Interval] = [Interval(3, 3, 'F')]

        for solution in self.solutions:
            actual_result = solution.please_conform(caps)

            self.assertEqual(expected_result, actual_result)
