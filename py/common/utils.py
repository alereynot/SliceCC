from typing import List, Tuple, Optional


def check_dimensions(dimension: Optional[Tuple], coordinates: Optional[List[Tuple[int, int]]]) -> bool:
    # Check with Allan if coordinates should be >= 0

    if not dimension:
        return False
    if not coordinates:
        return False

    clear = all(
        [(dimension[0] >= x >= 0) & (dimension[1] >= y >= 0) for x, y in coordinates]
    )

    return clear
