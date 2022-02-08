import re
from typing import List, Tuple

from py.common import constants


class ParseResult:
    def __init__(
        self,
        valid: bool = False,
        dimension: Tuple[int, int] = [],
        coordinates: List[Tuple[int, int]] = [],
        message: str = "",
    ):
        self.valid = valid
        self.dimension = dimension
        self.coordinates = coordinates
        self.message = message


def assemble_coords(coords: str, ret_val: ParseResult) -> bool:
    coord_lst = re.findall(r"\(.*?\)", coords)
    re_parenth = re.compile(r"[()]")

    return [re_parenth.sub("", x) for x in coord_lst]


def parse_arguments(argv: List) -> ParseResult:
    ret_val = ParseResult()
    if len(argv) == 1:
        ret_val.message = constants.ERR_NO_ARGUMENTS
        return ret_val

    dimension = argv[1].strip().split(" ")[0]
    coord_str = argv[1].replace(dimension, "").strip()

    coord_lst = assemble_coords(coord_str, ret_val)

    if not coord_lst[0]:
        ret_val.message = constants.ERR_NO_COORDINATES
        return ret_val

    coordinates = []
    for coord in coord_lst:
        val = coord.split(",")
        try:
            coordinates.append((int(val[0]), int(val[1])))
        except (ValueError, IndexError):
            ret_val.message = constants.ERR_INCOMPLETE_COORD
            return ret_val

    try:
        dimension_val = [int(x) for x in dimension.split("x")]
    except ValueError:
        ret_val.message = constants.ERR_INCOMPLETE_COORD
        return ret_val

    ret_val.valid = True
    ret_val.dimension = dimension_val
    ret_val.coordinates = coordinates
    return ret_val
