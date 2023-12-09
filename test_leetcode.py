import unittest
import utility
import time

# python3 -m unittest -v <.py>


class TestProcess(unittest.TestCase):

    def test_three_sum(self):
        class Format:
            def __init__(self, nums, wants) -> None:
                self.nums = nums
                self.wants = wants

        tests = []

        tests.append(Format([-1, 0, 1, 2, -1, -4], [[-1,-1,2],[-1,0,1]]))


if __name__ == '__main__':
    unittest.main()
