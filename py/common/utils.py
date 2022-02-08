from typing import List


def check_dimensions(dimension: List[int], coordinates) -> bool:
    clear_x = any([True for x in coordinates if x[0] > dimension[0]])
    clear_y = any([True for y in coordinates if y[1] > dimension[1]])

    return clear_x | clear_y
