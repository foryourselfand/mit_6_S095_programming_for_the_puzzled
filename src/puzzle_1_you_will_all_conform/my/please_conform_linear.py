from typing import List

from structures import Interval


class PleaseConformLinear:
    def please_conform_linear(self, caps: List[str]) -> List[Interval]:
        if len(caps) == 0:
            return list()

        caps: List[str] = caps.copy()

        cap_first: str = caps[0]
        caps.append(cap_first)

        interval_results: List[Interval] = list()
        interval_start: int = 0

        for index_current in range(1, len(caps)):
            index_previous = index_current - 1

            cap_current: str = caps[index_current]
            cap_previous: str = caps[index_previous]

            if cap_current != cap_previous:
                if cap_current != cap_first:
                    interval_start = index_current

                interval_result = Interval(interval_start, index_previous, cap_previous)
                interval_results.append(interval_result)

        return interval_results
