"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

    def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that
 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3

the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

import unittest
from collections import defaultdict


def solution(A: list) -> list:
    if not A:
        return -1

    occurrencies = defaultdict(lambda: {'count': 0, 'index': -1})

    for index, elem in enumerate(A):
        if not occurrencies[elem]['count']:
            occurrencies[elem]['index'] = index

        occurrencies[elem]['count'] += 1

    dominator_candidate = sorted(occurrencies.keys(),
                                 key=lambda key: occurrencies[key]['count'],
                                 reverse=True)[0]

    occurrence = occurrencies[dominator_candidate]

    if occurrence['count'] > len(A) / 2:
        return occurrence['index']
    else:
        return -1


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        A = [3, 4, 3, 2, 3, -1, 3, 3]
        result = solution(A)
        self.assertIn(result, [0, 2, 4, 6, 7])

    def test_case_2(self):
        A = [5, 4, 3, 2, 3, -1, 3, 3]
        result = solution(A)
        self.assertIn(result, [-1])

    def test_case_3(self):
        A = []
        result = solution(A)
        self.assertIn(result, [-1])


if __name__ == "__main__":
    unittest.main()
