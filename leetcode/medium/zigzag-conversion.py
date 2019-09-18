"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
 A P L S I I G
  Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I     N
 A   L S   I G
  Y A   H R
   P     I
"""


def convert(s: str, numRows: int) -> str:
    ret = ""
    lines = []
    for _ in range(numRows):
        lines.append("")
    for i, x in enumerate(s):
        """
        count blanks from the expected:
        t     s
         e   e t   t
          s t   t s
           t     e
        0 1 2 3 1 3 5 1 3 5 1 3 5
        so
        |0123| /135/ /135/ /135/
        The number of blanks could be summarized as:
        # The first slope: 
        i
        # The following slope:
            generate a list[int] which is (numRows - 1) long as the numbers of blanks:
            for _ in range(numRows-1): nums_b.append((_+1) * 2 - 1)
            
            num_blanks = nums_b[(i - numRows) % (len(nums_b))]
        """
        if i <= numRows:
            num_blanks = i
        else:
            nums_b = []
            for _ in range(numRows - 1): nums_b.append((_ + 1) * 2 - 1)
            num_blanks = nums_b[(i - numRows) % (len(nums_b))]
            # which line should char x be in: i%numRows
        lines[i % numRows] += " "*num_blanks + x
    for line in lines:
        ret += line + "\n"
    return ret


inp = "testtesttset"
n_R = 4
print(convert(inp, n_R))
"""
expected:
t     s
 e   e t   t
  s t   t s
   t     e
"""
