"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 60 oranges among five ranks of nobles (公, 侯, 伯, 子, 男) such that each rank gets an additional 3 oranges compared to the rank below it. Let's compute the solution step by step.


"""


from fractions import Fraction

# Total oranges
total_oranges = 60

# The additional oranges for each rank
additional_oranges = [15, 12, 9, 6, 3]  # 公, 侯, 伯, 子, 男

# Sum of the additional oranges
sum_additional_oranges = sum(additional_oranges)

# Remaining oranges after distributing the additional ones
remaining_oranges = total_oranges - sum_additional_oranges

# Each rank gets an equal share of the remaining oranges
equal_share = remaining_oranges // 5

# Compute the total oranges for each rank
a = equal_share + additional_oranges[0]  # 公
b = equal_share + additional_oranges[1]  # 侯
c = equal_share + additional_oranges[2]  # 伯
d = equal_share + additional_oranges[3]  # 子
e = equal_share + additional_oranges[4]  # 男

# Results
a = Fraction(a)
b = Fraction(b)
c = Fraction(c)
d = Fraction(d)
e = Fraction(e)

# The solution
a, b, c, d, e


"""


This code calculates the number of oranges each rank receives (`a`, `b`, `c`, `d`, `e`) and represents the solution using the `Fraction` class.
"""


"""
"""
