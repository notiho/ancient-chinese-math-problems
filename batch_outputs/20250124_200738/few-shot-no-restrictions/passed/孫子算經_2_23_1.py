"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges. Each person receives an additional 3 oranges compared to the rank below them.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people (5) and add 3 oranges for each rank below the top.
Then assign 6 oranges to the lowest rank, 9 to the next, 12 to the next, 15 to the next, and 18 to the top rank.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined values for each rank:
- The top rank (Gong) receives 18 oranges.
- The second rank (Hou) receives 15 oranges.
- The third rank (Bo) receives 12 oranges.
- The fourth rank (Zi) receives 9 oranges.
- The fifth rank (Nan) receives 6 oranges.

Answer: The Gong receives *a* oranges, the Hou receives *b* oranges, the Bo receives *c* oranges, the Zi receives *d* oranges, and the Nan receives *e* oranges.
"""

# Total number of oranges
總橘子 = 60

# Number of ranks
人數 = 5

# Additional oranges for each rank
加橘子 = 3

# Assign base oranges for each rank
男 = 6
子 = 男 + 加橘子
伯 = 子 + 加橘子
侯 = 伯 + 加橘子
公 = 侯 + 加橘子

# Combine all base oranges
副并 = 男 + 子 + 伯 + 侯 + 公

# Subtract from total oranges
餘橘子 = 總橘子 - 副并

# Divide remainder among all ranks
每人加橘子 = 餘橘子 // 人數

# Final distribution
a = 公 + 每人加橘子
b = 侯 + 每人加橘子
c = 伯 + 每人加橘子
d = 子 + 每人加橘子
e = 男 + 每人加橘子

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
