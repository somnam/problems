"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

    def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5

the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        the elements of A are all distinct;
        each element of array A is an integer within the range [1..(N + 1)].

"""
import unittest


def solution(A):
    missing_candidates = set(range(1, len(A) + 2))
    missing_elements = missing_candidates.difference(A)
    return missing_elements.pop() if missing_elements else None


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        A = [2, 3, 1, 5]
        self.assertEqual(solution(A), 4)

    def test_case_2(self):
        A = [1, 2]
        self.assertEqual(solution(A), 3)

    def test_case_3(self):
        A = []
        self.assertEqual(solution(A), 1)


if __name__ == "__main__":
    unittest.main()
