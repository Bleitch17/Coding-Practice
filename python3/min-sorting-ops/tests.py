import unittest

from solution import Solution


class TestMinSortingOps(unittest.TestCase):
    def setUp(self) -> None:
        self._solution: Solution = Solution()
    
    def test_example_1(self) -> None:
        self.assertEqual(1, self._solution.get_min_operations([3, 3, 2]))

    def test_example_2(self) -> None:
        self.assertEqual(3, self._solution.get_min_operations([2, 3, 2, 5, 4]))

    def test_already_sorted(self) -> None:
        nums: list[int] = [i for i in range(100)]

        self.assertEqual(0, self._solution.get_min_operations(nums))


if __name__ == "__main__":
    unittest.main()