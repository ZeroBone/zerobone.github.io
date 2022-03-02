from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class ZBLogo(Scene):
    def construct(self):

        vertices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        edges = [("1", "2"), ("2", "3"), ("2", "7"), ("5", "2"), ("3", "6"), 
            ("5", "4"), ("5", "6"), ("8", "5"), ("6", "9"),
            ("7", "8"), ("9", "8")]

        layout_scale = 2
        
        lt = {
            "1": np.array([-1, 1, 0]) * layout_scale,
            "2": np.array([0, 1, 0]) * layout_scale,
            "3": np.array([.75, 1, 0]) * layout_scale,
            "4": np.array([-1, 0, 0]) * layout_scale,
            "5": np.array([0, 0, 0]) * layout_scale,
            "6": np.array([.75, 0, 0]) * layout_scale,
            "7": np.array([-1, -1, 0]) * layout_scale,
            "8": np.array([0, -1, 0]) * layout_scale,
            "9": np.array([.75, -1, 0]) * layout_scale
        }

        stroke_w = 2

        vc = {
            "1": {"fill_color": BLUE, "stroke_width": stroke_w},
            "2": {"fill_color": PINK, "stroke_width": stroke_w},
            "3": {"fill_color": GREEN, "stroke_width": stroke_w},
            "4": {"fill_color": GREEN, "stroke_width": stroke_w},
            "5": {"fill_color": RED, "stroke_width": stroke_w},
            "6": {"fill_color": YELLOW, "stroke_width": stroke_w},
            "7": {"fill_color": TEAL_E, "stroke_width": stroke_w},
            "8": {"fill_color": PURPLE, "stroke_width": stroke_w},
            "9": {"fill_color": WHITE, "stroke_width": stroke_w},
        }

        edge_stroke_w = 10

        ec = {
            edges[0]: {"stroke_color": RED, "angle": 0, "stroke_width": edge_stroke_w},
            edges[2]: {"stroke_color": RED, "angle": 0, "stroke_width": edge_stroke_w},
            edges[9]: {"stroke_color": RED, "angle": 0, "stroke_width": edge_stroke_w},
            edges[1]: {"stroke_color": GOLD, "angle": 0, "stroke_width": edge_stroke_w},
            edges[3]: {"stroke_color": GOLD, "angle": 0, "stroke_width": edge_stroke_w},
            edges[4]: {"stroke_color": GOLD, "angle": -PI/2, "stroke_width": edge_stroke_w},
            edges[6]: {"stroke_color": GOLD, "angle": 0, "stroke_width": edge_stroke_w},
            edges[7]: {"stroke_color": GOLD, "angle": 0, "stroke_width": edge_stroke_w},
            edges[8]: {"stroke_color": GOLD, "angle": -PI/2, "stroke_width": edge_stroke_w},
            edges[10]: {"stroke_color": GOLD, "angle": 0, "stroke_width": edge_stroke_w},
            edges[5]: {"stroke_color": BLUE, "stroke_width": edge_stroke_w, "angle": 0}
        }

        lbl = "\\bullet"

        g = Graph(
            vertices,
            edges,
            layout=lt,
            labels={"1": lbl, "2": lbl, "3": lbl, "4": lbl, "5": lbl,
                "6": lbl, "7": lbl, "8": lbl, "9": lbl},
            vertex_config=vc,
            edge_config=ec,
            edge_type=CurvedArrow
        )

        self.add(g)
