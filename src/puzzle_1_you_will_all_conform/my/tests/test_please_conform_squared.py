from please_conform_squared import PleaseConformSquared
from test_please_conform import TestPleaseConform


class TestPleaseConformSquared(TestPleaseConform):
    def get_solution(self):
        return PleaseConformSquared()
