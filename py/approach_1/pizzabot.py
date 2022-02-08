import os
import sys
from typing import List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import constants
from common.sliceargparser import parse_arguments

from common.utils import check_dimensions


def moves(axis: str, pos: int, dest: int) -> str:
    ret_val = ""
    while pos != dest:
        if pos > dest:
            ret_val += constants.DIRECTIONS[axis + "-"]
            pos -= 1
        else:
            ret_val += constants.DIRECTIONS[axis + "+"]
            pos += 1
    return ret_val


def find_directions(dimension: List[int], coordinates: List[Tuple[int, int]]) -> str:

    if check_dimensions(dimension, coordinates):
        return constants.ERR_COORD_NOT_IN_GRID

    ret_val = ""
    x, y = 0, 0
    for coord in coordinates:
        dest_x, dest_y = coord[0], coord[1]

        ret_val += moves("x", x, dest_x)
        ret_val += moves("y", y, dest_y)
        x, y = dest_x, dest_y

        ret_val += constants.DROP

    return ret_val


def main():
    arguments = parse_arguments()

    if not arguments.valid:
        print(arguments.message)
        return

    directions = find_directions(arguments.dimension, arguments.coordinates)
    print(directions)
    return


if __name__ == "__main__":
    main()
