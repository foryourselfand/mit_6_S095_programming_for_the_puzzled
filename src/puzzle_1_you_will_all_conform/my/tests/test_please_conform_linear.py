from unittest import TestCase

from please_conform_linear import PleaseConformLinear


class TestPleaseConformLinear(TestCase):
    def setUp(self) -> None:
        self.solution = PleaseConformLinear()
