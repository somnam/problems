"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).
"""
import unittest
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = self.merge_arrays(nums1, nums2)

        return self.calculate_median(nums3)

    def calculate_median(self, nums3: List[int]) -> float:
        len_nums3 = len(nums3)
        if len_nums3 % 2 != 0:
            idx = (len_nums3 // 2)
            median = nums3[idx] * 1.0
        else:
            idx_l = (len_nums3 // 2) - 1
            idx_p = idx_l + 1
            median = (nums3[idx_l] + nums3[idx_p]) / 2

        return median

    def merge_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx1 = 0
        idx2 = 0
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        nums3 = []

        while (idx1 < len_nums1 or idx2 < len_nums2):
            if idx1 == len_nums1:
                nums3.append(nums2[idx2])
                idx2 += 1
            elif (idx2 == len_nums2) or (nums1[idx1] < nums2[idx2]):
                nums3.append(nums1[idx1])
                idx1 += 1
            elif nums2[idx2] < nums1[idx1]:
                nums3.append(nums2[idx2])
                idx2 += 1
            else:
                nums3.append(nums1[idx1])
                nums3.append(nums2[idx2])
                idx1 += 1
                idx2 += 1

        return nums3


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.0)

    def test_case_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.5)

    def test_case_3(self):
        nums1 = [0, 0]
        nums2 = [0, 0]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 0.0)

    def test_case_4(self):
        nums1 = []
        nums2 = [1]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 1.0)

    def test_case_5(self):
        nums1 = [2]
        nums2 = []
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 2.0)

    def test_case_6(self):
        nums1 = [2, 5, 6]
        nums2 = [4, 7, 8, 9]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 6.0)

    def test_case_7(self):
        nums1 = [2, 5, 6]
        nums2 = [4, 7, 8]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 5.5)

    def test_case_8(self):
        nums1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4]
        nums2 = [1, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        result = Solution().findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, 3.0)


if __name__ == '__main__':
    unittest.main()
