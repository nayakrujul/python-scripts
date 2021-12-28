import matplotlib.pyplot as plt
import numpy as np
import QuadraticEquationSolver


def show_graph(x, y):
    plt.plot(np.array(x), np.array(y))
    plt.show()


def get_points(self, turn):

    x = [w / 2 for w in list(range(int((turn[0] - 10) * 2), int((turn[0] + 11) * 2)))]
    y = [self.get_y(z) for z in x]
    return [x, y]


eq = QuadraticEquationSolver.Equation()
if eq.allowed:
    if eq.Solve():
        show_graph(
            get_points(eq, QuadraticEquationSolver.turning_point(eq.x1, eq.x2, eq.a, eq.b, eq.c))[0],
            get_points(eq, QuadraticEquationSolver.turning_point(eq.x1, eq.x2, eq.a, eq.b, eq.c))[1]
        )
