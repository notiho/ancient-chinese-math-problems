"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges.
Each person is to receive 3 more oranges than the person ranked below them.
Question: how many oranges does each of the five ranks receive?

The procedure says:
First, place the number of people, each with an additional 3 oranges below them:
- The lowest gets 6 oranges,
- The next gets 9 oranges,
- The next gets 12 oranges,
- The next gets 15 oranges,
- The highest gets 18 oranges.
Add these together, obtaining 45.
Subtract this from the total of 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts:
- The highest rank (Gong) gets 18 oranges,
- The next rank (Hou) gets 15 oranges,
- The next rank (Bo) gets 12 oranges,
- The next rank (Zi) gets 9 oranges,
- The lowest rank (Nan) gets 6 oranges.

Answer: Gong gets *a* oranges, Hou gets *b* oranges, Bo gets *c* oranges, Zi gets *d* oranges, Nan gets *e* oranges.
"""

# Total oranges
總橘子 = 60

# Additional oranges per rank
加橘子 = 3

# Base distribution for each rank
男 = 6
子 = 男 + 加橘子
伯 = 子 + 加橘子
侯 = 伯 + 加橘子
公 = 侯 + 加橘子

# Combine the base distribution
副和 = 男 + 子 + 伯 + 侯 + 公

# Remaining oranges after base distribution
餘橘子 = 總橘子 - 副和

# Distribute the remainder equally among the 5 people
每人加 = 餘橘子 // 5

# Final distribution
a = 公 + 每人加
b = 侯 + 每人加
c = 伯 + 每人加
d = 子 + 每人加
e = 男 + 每人加

# Output the results
a, b, c, d, e#----- content ends here -----

"""
"""
