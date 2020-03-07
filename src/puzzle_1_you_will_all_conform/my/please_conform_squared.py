from typing import List

from please_conform import PleaseConform
from structures import Interval


class PleaseConformSquared(PleaseConform):
    def please_conform(self, caps: List[str]) -> List[Interval]:
        if len(caps) == 0:
            return list()

        caps: List[str] = caps.copy()

        caps.append('end')

        interval_inputs: List[Interval] = list()
        count_forward: int = 0
        count_backward: int = 0
        index_previous: int = 0

        for index_current in range(1, len(caps)):
            cap_current = caps[index_current]
            cap_previous = caps[index_previous]

            if cap_current != cap_previous:
                interval_input = Interval(start=index_previous,
                                          end=index_current - 1,
                                          cap_type=cap_previous)
                interval_inputs.append(interval_input)

                if cap_previous == 'F':
                    count_forward += 1
                else:
                    count_backward += 1
                index_previous = index_current

        cap_to_flip: str
        if count_forward < count_backward:
            cap_to_flip = 'F'
        else:
            cap_to_flip = 'B'

        interval_results: List[Interval] = list()

        for interval_input in interval_inputs:
            if interval_input.cap_type == cap_to_flip:
                interval_result: Interval = interval_input
                interval_results.append(interval_result)

        return interval_results
