"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:
  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0

There are eleven (unordered) pairs of discs that intersect, namely:

        discs 1 and 4 intersect, and both intersect with all the other discs;
        disc 2 also intersects with discs 0 and 3.

Write a function:

    def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [0..2,147,483,647].
"""

import unittest


def solution(A: list):
    class Disc:
        def __init__(self, center: int, radius: int) -> None:
            self.center = center
            self.radius = radius
            self.start = center - radius
            self.end = center + radius

        def intersect(self, other: object) -> bool:
            return (
                other.start <= self.center <= other.end
                or other.start <= self.start <= other.end
                or other.start <= self.end <= other.end
            )

        def __repr__(self):
            return f"Disc(center={self.center}, radius={self.radius})"

        def __eq__(self, other):
            return self.center == other.center and self.radius == other.radius

        def __lt__(self, other):
            return self.center <= other.center or self.end <= other.end

    discs = [Disc(i, r) for i, r in enumerate(A)]

    sorted_asc = sorted(discs)
    sorted_desc = list(reversed(sorted_asc))

    pairs = 0
    for start_disc in sorted_asc:
        for end_disc in sorted_desc:
            if start_disc == end_disc:
                break
            if start_disc.intersect(end_disc):
                pairs += 1

    return pairs


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        A = [1, 5, 2, 1, 4, 0]

        result = solution(A)

        self.assertEqual(result, 11)

    def test_case_2(self):
        A = [1, 1, 1]

        result = solution(A)

        self.assertEqual(result, 3)

    def test_case_3(self):
        A = [1, 10, 100, 1]

        result = solution(A)

        self.assertEqual(result, 5)

    def test_case_4(self):
        A = [1, 2, 3]

        result = solution(A)

        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
