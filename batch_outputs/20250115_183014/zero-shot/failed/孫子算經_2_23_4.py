"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 60 oranges among five ranks of nobles (公, 侯, 伯, 子, 男) such that each rank receives 3 more oranges than the rank below it. We will compute the number of oranges each rank receives.

Here is the Python code:


"""


from fractions import Fraction

# Total number of oranges
total_oranges = 60

# The difference in oranges between each rank
difference = 3

# Calculate the total weight of the coefficients
coefficients_sum = 5 + 4 + 3 + 2 + 1  # 公 + 侯 + 伯 + 子 + 男

# Calculate the base number of oranges for the lowest rank (男)
e = Fraction(total_oranges - difference * coefficients_sum, 5)

# Calculate the number of oranges for each rank
d = e + difference  # 子
c = d + difference  # 伯
b = c + difference  # 侯
a = b + difference  # 公

# The results
a, b, c, d, e


"""


### Explanation of the Code:
1. The total number of oranges is 60.
2. Each rank receives 3 more oranges than the rank below it.
3. The coefficients for the ranks are 5, 4, 3, 2, and 1 (公, 侯, 伯, 子, 男 respectively).
4. We calculate the base number of oranges for the lowest rank (男) using the formula:
   \[
   e = \frac{\text{total oranges} - (\text{difference} \times \text{coefficients sum})}{5}
   \]
5. Using the base value \(e\), we calculate the number of oranges for the other ranks by adding the difference iteratively.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will contain the number of oranges for 公, 侯, 伯, 子, and 男 respectively.
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 15
Variable 'b' has wrong value. Expected: 15, Actual: 12
Variable 'c' has wrong value. Expected: 12, Actual: 9
Variable 'd' has wrong value. Expected: 9, Actual: 6
Variable 'e' has wrong value. Expected: 6, Actual: 3"""
