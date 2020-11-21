from typing import List, Tuple

from render.render_base import RenderBase


class ConsoleRender(RenderBase):

    def render(self, positions: List[Tuple[int, int]]) -> None:
        print("===================")
        for i in range(8):
            print("| ", end='')
            for j in range(8):
                queen_at_position = False

                for p1, p2 in positions:
                    if i == p1 and j == p2:
                        queen_at_position = True

                if queen_at_position:
                    char = 'D'
                else:
                    if j % 2 == i % 2:
                        char = '.'
                    else:
                        char = '#'

                print(char + ' ', end='')
            print("|")
        print("===================")
