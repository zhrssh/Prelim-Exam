import unittest

class MyTest(unittest.TestCase):
    def test_check(self):
        name = "PEDRO"
        self.assertEqual(name, "PEDRO", "Name is not \"PEDRO\"")

if __name__ == "__main__":
    unittest.main()