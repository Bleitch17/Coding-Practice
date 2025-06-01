import unittest

from solution import Solution


class TestMinSortingOps(unittest.TestCase):
    def setUp(self) -> None:
        self._solution: Solution = Solution()
    
    def test_example_1(self) -> None:
        self.assertEqual(4, self._solution.password_variability("abc"))

    def test_example_2(self) -> None:
        self.assertEqual(9, self._solution.password_variability("abcab"))

    def test_3_pairs_same_letter(self) -> None:
        self.assertEqual(19, self._solution.password_variability("evileye"))


if __name__ == "__main__":
    unittest.main()