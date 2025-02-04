"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges such that each person receives 3 more oranges than the person ranked below them.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people (5) and add 3 oranges for each rank below:
- The lowest rank (Nan) gets 6 oranges.
- The next rank (Zi) gets 9 oranges.
- The next rank (Bo) gets 12 oranges.
- The next rank (Hou) gets 15 oranges.
- The highest rank (Gong) gets 18 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder.
Divide the remainder evenly among the 5 people, and add the result to the base distribution.

Answer: The Gong receives *a* oranges, the Hou receives *b* oranges, the Bo receives *c* oranges, the Zi receives *d* oranges, and the Nan receives *e* oranges.
"""

# Total oranges
總橘子 = 60

# Base distribution for each rank
男分 = 6
子分 = 9
伯分 = 12
侯分 = 15
公分 = 18

# Sum of the base distribution
基礎分配總數 = 男分 + 子分 + 伯分 + 侯分 + 公分

# Remaining oranges after base distribution
剩餘橘子 = 總橘子 - 基礎分配總數

# Distribute the remainder evenly among 5 people
每人加橘子 = Fraction(剩餘橘子, 5)

# Final distribution
e = 男分 + 每人加橘子  # 男
d = 子分 + 每人加橘子  # 子
c = 伯分 + 每人加橘子  # 伯
b = 侯分 + 每人加橘子  # 侯
a = 公分 + 每人加橘子  # 公

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
