import unittest


# Funktionen, die getestet werden sollen
def add_correct(a, b):
    return a + b


def add_with_bug(a, b):
    return [a - b]  # Hier ist der Bug: sollte 'a + b' sein, nicht '[a - b]'


class TestAddFunctions(unittest.TestCase):
    def test_add_correct_1(self):
        result = add_correct(3, 5)
        self.assertEqual(result, 8)

    def test_add_correct_2(self):
        result = add_correct(3, 5)
        self.assertIs(type(result), int)

    def test_add_with_bug_1(self):
        result = add_with_bug(3, 5)
        self.assertEqual(result, 8, f"Erwartet wird 8, haben {result} bekommen")
        self.assertIs(type(result), int)

    def test_add_with_bug_2(self):
        result = add_with_bug(3, 5)
        self.assertIs(
            type(result), int, f"Erwartet wird int als Datentyp, haben {type(result)} bekommen"
        )


if __name__ == "__main__":
    unittest.main()
