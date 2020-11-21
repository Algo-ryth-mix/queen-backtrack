from game.rules import queen_rule
from game.solver import Solver
from render.console_render import ConsoleRender

if __name__ == '__main__':
    x = ConsoleRender()

    queen_data = [(0, 0)]
    (success, solution) = Solver.solve(queen_data, queen_rule)

    if success:
        x.render(solution)

    print("D=Queen")
