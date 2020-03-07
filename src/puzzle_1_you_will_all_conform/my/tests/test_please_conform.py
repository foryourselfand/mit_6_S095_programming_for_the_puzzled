from typing import List
from unittest import TestCase

from please_conform import PleaseConform
from please_conform_linear import PleaseConformLinear
from please_conform_squared import PleaseConformSquared


class TestPleaseConform(TestCase):
    def setUp(self) -> None:
        self.solutions: List[PleaseConform] = list()
        self.solutions.append(PleaseConformSquared())
        self.solutions.append(PleaseConformLinear())

    def test_empty(self):
        caps: List[str] = list()

        expected_result = list()
        expected_result_len = 0

        for solution in self.solutions:
            actual_result = solution.please_conform(caps)
            actual_result_len = len(actual_result)

            self.assertEqual(expected_result, actual_result)
            self.assertEqual(expected_result_len, actual_result_len)
