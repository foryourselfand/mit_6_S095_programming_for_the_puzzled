from typing import List
from unittest import TestCase

from please_conform_squared import PleaseConformSquared


class TestPleaseConformSquared(TestCase):
    def setUp(self) -> None:
        self.solution = PleaseConformSquared()

    def test_empty(self):
        caps: List[str] = list()

        expected_result = list()
        expected_result_len = 0

        actual_result = self.solution.please_conform(caps)
        actual_result_len = len(actual_result)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_result_len, actual_result_len)
