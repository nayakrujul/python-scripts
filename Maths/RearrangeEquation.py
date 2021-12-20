from string import ascii_letters


def simplify(eq):

    left, right = eq.split(" ÷ ")
    for letter in ascii_letters:
        if len(left.split(letter)) > 2:
            try:
                left = f"({int(left.split(letter)[0][1:]) + int(left.split(letter)[1])}{letter})"
            except:
                pass
    return f"{left} ÷ {right}"


def rearrange(equation: str, subject: str):

    try:

        equation = equation.replace("-", "+-")

        left, right = equation.split("=")
        if subject in right:
            left, right = right, left

        left1 = left.split("+")[0]
        left2 = left.split("+")[1]
        if subject in left2:
            left1, left2 = left2, left1

        if left2[0] == "-":
            right += "+" + left2[1:]
        else:
            right += "-" + left2.replace("+", "")

        coefficient = left1.split(subject)[0]
        new_right = simplify(f"({right}) ÷ {coefficient}")
        return f"{subject} = {new_right}"

    except:

        return "Wrong format"


print(rearrange("5x+10y=78", "x"))
print(rearrange("5x+10y=78y", "x"))
print(rearrange("5x+10y=78z", "x"))
print(rearrange("5x+10y=78", "y"))
print(rearrange("5x+10y=78z", "y"))
