import unittest
import main


class MyTestCase(unittest.TestCase):

    def test_1(self):
        inputs = ("H", "O", "H2", "CO2", "CH4", "C6 H12 O6", "HNO3")
        want = (1, 16, 2, 44, 16, 180, 63)
        for x in range(len(inputs)):
            self.assertEqual(int(round(main.get_mass(inputs[x])[0])), want[x])

    def test_2(self):
        inputs = ("H", "O", "H2", "CO2", "CH4", "C6 H12 O6", "HNO3")
        want = (
            (0, 1, 1),
            (8, 8, 8),
            (0, 2, 2),
            (22, 22, 22),
            (6, 10, 10),
            (84, 96, 96),
            (31, 32, 32)
        )
        for x in range(len(inputs)):
            self.assertEqual(main.get_mass(inputs[x])[1:], want[x])


if __name__ == '__main__':
    unittest.main()
