"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

    def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3, because the frog will be positioned as follows:

        after the first jump, at position 10 + 30 = 40
        after the second jump, at position 10 + 30 + 30 = 70
        after the third jump, at position 10 + 30 + 30 + 30 = 100

Write an efficient algorithm for the following assumptions:

        X, Y and D are integers within the range [1..1,000,000,000];
        X ≤ Y.

"""
import unittest


def solution(X, Y, D):
    distance = Y - X
    steps = distance // D

    # One last step.
    if (steps * D) < distance:
        steps += 1

    return steps


class SolutionTests(unittest.TestCase):
    def test_case_0(self):
        X, Y, D = 85, 85, 30
        self.assertEqual(solution(X, Y, D), 0)

    def test_case_1(self):
        X, Y, D = 10, 85, 30
        self.assertEqual(solution(X, Y, D), 3)

    def test_case_2(self):
        X, Y, D = 1, 512, 4
        self.assertEqual(solution(X, Y, D), 128)


if __name__ == "__main__":
    unittest.main()
