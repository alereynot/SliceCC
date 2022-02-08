import sys
from typing import List, Tuple

from py.common import constants
from py.common.sliceargparser import parse_arguments
from py.common.utils import check_dimensions


def moves(x: int, y: int, dest: Tuple) -> str:
    keep_going = not ((x == dest[0]) & (y == dest[1]))
    ret_val = ""

    while keep_going:
        if x > dest[0]:
            ret_val += constants.MOVE_WEST
            x -= 1
        elif x < dest[0]:
            ret_val += constants.MOVE_EAST
            x += 1
        if y > dest[1]:
            ret_val += constants.MOVE_SOUTH
            y -= 1
        elif y < dest[1]:
            ret_val += constants.MOVE_NORTH
            y += 1
        keep_going = not ((x == dest[0]) & (y == dest[1]))

    return ret_val


def find_directions(
    dimension: List[Tuple[int, int]], coordinates: List[Tuple[int, int]]
) -> str:

    if not check_dimensions(dimension, coordinates):
        return constants.ERR_COORD_NOT_IN_GRID

    ret_val = ""
    x, y = 0, 0
    for coord in coordinates:
        dest_x, dest_y = coord

        ret_val += moves(x, y, coord)
        x, y = dest_x, dest_y

        ret_val += constants.DROP

    return ret_val


def main():
    arguments = parse_arguments(sys.argv)

    if not arguments.valid:
        print(arguments.message)
        return

    directions = find_directions(arguments.dimension, arguments.coordinates)
    print(directions)
    return


if __name__ == "__main__":
    main()
