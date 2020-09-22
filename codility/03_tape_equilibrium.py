"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

We can split this tape in four places:

        P = 1, difference = |3 − 10| = 7
        P = 2, difference = |4 − 9| = 5
        P = 3, difference = |6 − 7| = 1
        P = 4, difference = |10 − 3| = 7

Write a function:

    def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3

the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−1,000..1,000].
"""
import unittest


def solution(A):
    sum_A = sum(A)
    sum_left_part = 0
    sum_right_part = sum_A

    lowest_divide_difference = None
    for divide_idx in range(0, len(A) - 1):
        sum_left_part += A[divide_idx]
        sum_right_part -= A[divide_idx]
        divide_difference = abs(sum_left_part - sum_right_part)
        if lowest_divide_difference is None:
            lowest_divide_difference = divide_difference
            continue
        if divide_difference < lowest_divide_difference:
            lowest_divide_difference = divide_difference

    return lowest_divide_difference


class SolutionTest(unittest.TestCase):
    def test_case_1(self):
        A = [3, 1, 2, 4, 3]
        self.assertEqual(solution(A), 1)

    def test_case_2(self):
        A = [3, 1, 1]
        self.assertEqual(solution(A), 1)

    def test_case_3(self):
        A = [-1000, 1000]
        self.assertEqual(solution(A), 2_000)

    def test_case_4(self):
        A = [-10, -5, -3, -4, -5]
        self.assertEqual(solution(A), 3)

    def test_case_5(self):
        A = [-10, -20, -30, -40, 100]
        self.assertEqual(solution(A), 20)

    def test_case_6(self):
        A = [1, 2, 3, 4, 2]
        self.assertEqual(solution(A), 0)


if __name__ == "__main__":
    unittest.main()
