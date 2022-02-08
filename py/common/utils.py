from typing import List, Tuple


def check_dimensions(
    dimension: Tuple, coordinates: List[Tuple[int, int]]
) -> bool:

    # Check with Allan if coordinates should be >= 0
    clear = all(
        [(dimension[0] >= x >= 0) & (dimension[1] >= y >= 0) for x, y in coordinates]
    )

    return clear
