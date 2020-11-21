from .common import Piece


def tower_rule(tower: Piece, other: Piece) -> bool:
    t1, t2 = tower
    o1, o2 = other

    return (t1 % 8 == o1 % 8) or (t2 % 8 == o2 % 8)


def bishop_rule(bishop: Piece, other: Piece) -> bool:
    b1, b2 = bishop
    o1, o2 = other

    return abs(b1 - o1) == abs(b2 - o2)


def queen_rule(queen: Piece, other: Piece) -> bool:
    return tower_rule(queen, other) or bishop_rule(queen, other)
