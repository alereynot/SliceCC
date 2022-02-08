import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List, Tuple

from common import constants
from common.sliceargparser import parse_arguments
from common.utils import check_dimensions


def moves(position: Tuple, destination: Tuple) -> str:
    ret_val = ""
    x, y = position

    distance_x = destination[0] - x
    distance_y = destination[1] - y

    if distance_x > 0:
        ret_val += constants.MOVE_EAST * distance_x
    else:
        ret_val += constants.MOVE_WEST * abs(distance_x)

    if distance_y > 0:
        ret_val += constants.MOVE_NORTH * distance_y
    else:
        ret_val += constants.MOVE_SOUTH * abs(distance_y)

    ret_val += constants.DROP
    return ret_val


def find_directions(dimension: List[int], coordinates: List[Tuple[int, int]]) -> str:

    if check_dimensions(dimension, coordinates):
        return constants.ERR_COORD_NOT_IN_GRID

    ret_val = ""
    x, y = 0, 0
    for coord in coordinates:
        dest_x, dest_y = coord[0], coord[1]
        ret_val += moves((x, y), (dest_x, dest_y))
        x = dest_x
        y = dest_y

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
