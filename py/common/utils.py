from typing import List, Tuple


def check_dimensions(dimension: List[Tuple[int, int]], coordinates) -> bool:

    clear = all([(x <= dimension[0]) & (y <= dimension[1]) for x, y in coordinates])

    return clear
