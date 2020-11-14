"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
"""
import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        numColumns = self.get_num_columns(s, numRows)
        matrix = self.get_zig_matrix(s, numRows, numColumns)
        return self.get_zig_str(matrix)

    def get_zig_str(self, matrix: list) -> str:
        return "".join(
            matrix[idy][idx]
            for idx in range(len(matrix[0]))
            for idy in range(len(matrix))
            if matrix[idy][idx] is not False
        )

    def get_zig_matrix(self, s: str, numRows: int, numColumns: int) -> list:
        zig_columns = self.zig_columns(numRows)

        matrix = [[False for _ in range(numRows)] for _ in range(numColumns)]

        start_idx = 0
        end_idx = 0
        for col_idx, column in enumerate(matrix):
            is_full_column = col_idx % (numRows - 1) == 0 if numRows > 1 else True

            if is_full_column:
                start_idx = end_idx
                end_idx = start_idx + numRows
                for char_idx, char in enumerate(s[start_idx:end_idx]):
                    column[char_idx] = char

                zig_columns = self.zig_columns(numRows)
            else:
                zig_idx = zig_columns
                column[zig_idx] = s[end_idx]
                end_idx += 1
                zig_columns -= 1

        return matrix

    def get_num_columns(self, s: str, numRows: int) -> int:
        idx = 0
        columns = 0
        zig_columns = self.zig_columns(numRows)
        full_column = True
        while idx < len(s):
            if zig_columns == 0:
                full_column = True

            if full_column:
                idx += numRows
                full_column = False
                zig_columns = self.zig_columns(numRows)
            else:
                idx += 1
                zig_columns -= 1

            columns += 1

        return columns

    def zig_columns(self, numRows: int) -> int:
        zig_columns = numRows - 2
        return zig_columns if zig_columns > 0 else 0


class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        """
        P   A   H   N
        A P L S I I G
        Y   I   R

        [
            [P, None, A, None, H, None, N   ],
            [A, P,    L, S,    I, I,    G   ],
            [Y, None, I, None, R, None, None],

             0  1     2  3     4   5     6
            [0, None, 4, None, 8,  None, 12  ],
            [1, 3,    5, 7,    9,  11,   13  ],
            [2, None, 6, None, 10, None, None],
        ]
        """
        s = 'PAYPALISHIRING'
        numRows = 3
        result = Solution().convert(s, numRows)
        self.assertEqual(result, 'PAHNAPLSIIGYIR')

    def test_case_2(self):
        """
        P     I    N
        A   L S  I G
        Y A   H R
        P     I

        [
            [P, None, None, I, None, None, N   ],
            [A, None, L,    S, None, I,    G   ],
            [Y, A,    None, H, R,    None, None],
            [P, None, None, I, None, None, None],

             0  1     2     3  4     5     6
            [0, None, None, 6, None, None, 12  ],
            [1, None, 5,    7, None, 11,   13  ],
            [2, 4,    None, 8, 10,   None, None],
            [3, None, None, 9, None, None, None],

        ]
        """
        s = "PAYPALISHIRING"
        numRows = 4
        result = Solution().convert(s, numRows)
        self.assertEqual(result, 'PINALSIGYAHRPI')

    def test_case_3(self):
        s = "A"
        numRows = 1
        result = Solution().convert(s, numRows)
        self.assertEqual(result, 'A')

    def test_case_4(self):
        """
            [
                 0  1
                [A, B]
            ]
        """
        s = "AB"
        numRows = 1
        result = Solution().convert(s, numRows)
        self.assertEqual(result, 'AB')


if __name__ == "__main__":
    unittest.main()
