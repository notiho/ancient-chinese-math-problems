"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 60 oranges among five ranks of nobles (公, 侯, 伯, 子, 男) such that each rank receives 3 more oranges than the rank below it. We'll calculate the number of oranges each rank receives.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total number of oranges
total_oranges = 60

# Let the number of oranges received by the lowest rank (男) be e
e = Fraction(6)  # As given in the problem, 男 receives 6 oranges

# Each rank receives 3 more oranges than the rank below it
d = e + 3  # 子
c = d + 3  # 伯
b = c + 3  # 侯
a = b + 3  # 公

# Verify the total
assert a + b + c + d + e == total_oranges

# The results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. Start with the lowest rank (男, `e`), which is given as 6 oranges.
2. Each subsequent rank receives 3 more oranges than the rank below it.
3. Calculate the number of oranges for each rank step by step.
4. Verify that the total number of oranges distributed equals 60.
5. The results are stored in variables `a`, `b`, `c`, `d`, and `e` corresponding to 公, 侯, 伯, 子, and 男, respectively.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will hold the following values:
- `a = 18` (公 receives 18 oranges)
- `b = 15` (侯 receives 15 oranges)
- `c = 12` (伯 receives 12 oranges)
- `d = 9`  (子 receives 9 oranges)
- `e = 6`  (男 receives 6 oranges)
"""


"""
"""
