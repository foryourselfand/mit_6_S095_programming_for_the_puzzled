from please_conform_linear import PleaseConformLinear
from test_please_conform import TestPleaseConform


class TestPleaseConformLinear(TestPleaseConform):
    def get_solution(self):
        return PleaseConformLinear()
