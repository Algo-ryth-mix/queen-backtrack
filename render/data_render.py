from typing import List, Tuple

from render.render_base import RenderBase


class DataRender(RenderBase):
    def render(self, positions: List[Tuple[int, int]]) -> None:
        print("Positions: " , positions)
