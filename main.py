from typing import Tuple

from game.rules import queen_rule
from game.solver import Solver
from render.console_render import ConsoleRender
from render.data_render import DataRender
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Attempts to solve the queen problem using the given constraints")
    parser.add_argument("constraints", metavar="N", type=int, nargs='*',
                        help="pass the constraints you want the backtracking solver to work with here",
                        default=[])

    args = parser.parse_args()

    if len(args.constraints) % 2 != 0:
        print("Constraints must be 2 integers, but your list of constraints was not even!")
        exit(1)

    constraints = [(args.constraints[i], args.constraints[i + 1]) for i in range(0, len(args.constraints), 2)]

    print("constraints: ", constraints)

    (success, solution) = Solver.solve(constraints, queen_rule, DataRender())

    if success:
        ConsoleRender().render(solution)

    print("D=Queen")
