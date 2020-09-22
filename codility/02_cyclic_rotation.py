"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

    def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given
    A = [3, 8, 9, 7, 6]
    K = 3

the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

For another example, given
    A = [0, 0, 0]
    K = 1

the function should return [0, 0, 0]

Given
    A = [1, 2, 3, 4]
    K = 4

the function should return [1, 2, 3, 4]

Assume that:

        N and K are integers within the range [0..100];
        each element of array A is an integer within the range [−1,000..1,000].

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""
import unittest


def solution(A, K):
    # Identity operation.
    len_A = len(A)
    if not(A and K and K != len_A):
        return A

    # Rotate elements only once for K > list length.
    if K > len_A:
        K = K % len_A

    idx = len(A) - K

    return A[idx:] + A[:idx]


class SolutionTests(unittest.TestCase):
    def test_case_0(self):
        A = [3, 8, 9, 7, 6]
        K = 0
        result = solution(A, K)
        self.assertListEqual(result, [3, 8, 9, 7, 6])

    def test_case_1(self):
        A = [3, 8, 9, 7, 6]
        K = 1
        result = solution(A, K)
        self.assertListEqual(result, [6, 3, 8, 9, 7])

    def test_case_2(self):
        A = [3, 8, 9, 7, 6]
        K = 3
        result = solution(A, K)
        self.assertListEqual(result, [9, 7, 6, 3, 8])

    def test_case_3(self):
        A = [1, 2, 3, 4]
        K = 4
        result = solution(A, K)
        self.assertListEqual(result, [1, 2, 3, 4])

    def test_case_4(self):
        A = [1, 2, 3, 4]
        K = 5
        result = solution(A, K)
        self.assertListEqual(result, [4, 1, 2, 3])

    def test_case_5(self):
        A = [3, 8, 9, 7, 6]
        K = 8
        result = solution(A, K)
        self.assertListEqual(result, [9, 7, 6, 3, 8])

    def test_case_6(self):
        A = [1, 2, 3, 4, 5]
        K = 100
        result = solution(A, K)
        self.assertListEqual(result, [1, 2, 3, 4, 5])

    def test_case_7(self):
        A = [1, 1, 2, 3, 5]
        K = 42
        result = solution(A, K)
        self.assertListEqual(result, [3, 5, 1, 1, 2])

    def test_case_8(self):
        A = []
        K = 1
        result = solution(A, K)
        self.assertListEqual(result, [])


if __name__ == "__main__":
    unittest.main()