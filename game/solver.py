from typing import List, Tuple

from .common import Piece


class Solver:
    num_queens = 8
    board_size = 8

    @staticmethod
    def solve(constraints: List[Piece], rule) -> Tuple[bool, List[Piece]]:
        for i in range(Solver.board_size):
            for j in range(Solver.board_size):

                valid_for_all_constraints = True

                for constraint in constraints:
                    if rule(constraint, (i, j)):
                        valid_for_all_constraints = False
                        break

                if not valid_for_all_constraints:
                    continue

                if len(constraints) + 1 >= Solver.num_queens:
                    return True, constraints + [(i, j)]

                (success, inner) = Solver.solve(constraints + [(i, j)], rule)
                if success:
                    return success, inner

        return False, []
