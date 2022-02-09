import sys
from typing import List, Tuple, Optional

from py.common import constants
from py.common.sliceargparser import parse_arguments
from py.common.utils import check_dimensions


def moves(position: Tuple, destination: Tuple) -> str:
    ret_val = ""
    x, y = position

    distance_x = destination[0] - x
    distance_y = destination[1] - y

    sign = "+" if distance_x > 0 else "-"
    ret_val += constants.DIRECTIONS["x" + sign] * distance_x

    sign = "+" if distance_y > 0 else "-"
    ret_val += constants.DIRECTIONS["y" + sign] * distance_y

    ret_val += constants.DROP
    return ret_val


def find_directions(
    dimension: Optional[Tuple], coordinates: Optional[List[Tuple[int, int]]]
) -> str:

    if not check_dimensions(dimension, coordinates):
        return constants.ERR_COORD_NOT_IN_GRID

    ret_val = ""
    x, y = 0, 0
    if not coordinates:
        return ret_val

    for coord in coordinates:
        dest_x, dest_y = coord
        ret_val += moves((x, y), (dest_x, dest_y))
        x = dest_x
        y = dest_y

    return ret_val


def main() -> None:
    arguments = parse_arguments(sys.argv)

    if not arguments.valid:
        print(arguments.message)
        return

    directions = find_directions(arguments.dimension, arguments.coordinates)
    print(directions)


if __name__ == "__main__":
    main()
