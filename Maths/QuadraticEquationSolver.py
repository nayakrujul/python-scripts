from math import sqrt


def convert(dec):
    if dec == float(int(dec)):
        return int(dec)
    for i in range(1, 1000000):
        # Accounting for the slight error in Python's float
        if (dec * i) % 1 < 0.001 or (dec * i) % 1 > 0.999:
            return f"{int(round(dec*i))}/{i} ({round(dec,4)})"
    return dec


def turning_point(x1, x2, a, b, c, conv=0):
    x = (x1 + x2) / 2
    y = (a * (x ** 2)) + (b * x) + c
    if conv:
        return convert(x), convert(y)
    else:
        return x, y


class Equation:

    def __init__(self):

        print("y = ax^2 + bx + c\n")

        self.allowed = True

        try:
            self.a = float(input("a = "))
            self.b = float(input("b = "))
            self.c = float(input("c = "))
        except Exception:
            self.allowed = False
            print("\nInvalid.")

    def Solve(self):

        # x = ( -b ± ( sqrt( ( b ** 2 ) - ( 4 * a * c ) ) ) ) / (2 * a)

        try:
            self.x1 = (-self.b + (sqrt((self.b ** 2) - (4 * self.a * self.c)))) / (2 * self.a)
            self.x2 = (-self.b - (sqrt((self.b ** 2) - (4 * self.a * self.c)))) / (2 * self.a)
        except:
            print("\nUnsolvable.")
            return False
        else:
            if self.x1 != self.x2:
                print(f"\nThe roots of the quadratic (the x-intercepts) are "
                      f"{convert(self.x1)} and {convert(self.x2)}.\n")
            else:
                print(f"\nThe root of the equation (the x-intercept) is {convert(self.x1)}.\n")
            print("Information about the graph:")
            if self.a > 0:
                print(" - The parabola goes up from the turning point.")
            elif self.a < 0:
                print(" - The parabola goes down from the turning point.")
            else:
                # This one shouldn't happen (should say "Unsolvable"), but it's there just in case
                print(" - It is a straight line.")
            print(f" - The y-intercept is (0, {convert(self.c)}).")
            print(f" - The turning point of the parabola is {turning_point(self.x1,self.x2,self.a,self.b,self.c, 1)}.")
            return True

    def get_y(self, x):

        return (self.a * (x ** 2)) + (self.b * x) + self.c


def main():

    eq = Equation()
    if eq.allowed:
        eq.Solve()
