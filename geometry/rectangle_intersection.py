"""
                         ___
                        |   |     ...
         _______________|___|___  ...
        |               |   |   | ...
        |               |   |   | ...
        |      B        | C |   | ...
        |               |   |   | ...
        |               |   |   | ...
    ____|_______________|___|___| ...
   |  A |               |   |     ...
   |____|               |___|     ...

    Check if two rectangles have a non-empty intersection. If the intersection is non-empty,
    return the rectangle formed by their intersection

    Possible scenarios on intersection:
    1 - partial overlap
    2 - one contains another
    3 - share common side
    4 - share common corner
    5 - form a cross
    6 - form a tee
    etc.

    Focus on conditions under which it can be guaranteed  that the rectangles do not intersect.
"""
from collections import namedtuple


Rect = namedtuple('Rect', ('x', 'y', 'width', 'height'))

def check_overlap(r1: Rect, r2: Rect) -> Rect:
    def is_intersect(r1, r2):
        return (r1.x <= r2.x)