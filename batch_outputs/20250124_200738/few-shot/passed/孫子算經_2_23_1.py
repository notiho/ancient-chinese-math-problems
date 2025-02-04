"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of nobles, and they are to divide 60 oranges. Each person is to receive 3 more oranges than the person below them.
Question: how many oranges does each of the five people receive?

The procedure says: First, place the number of people, adding 3 oranges for each rank below:
- The lowest gets 3 oranges,
- The next gets 6 oranges,
- The next gets 9 oranges,
- The next gets 12 oranges,
- The highest gets 15 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person. Add this to the uncombined amounts:
- The highest gets 18 oranges as the "Gong" share,
- The next gets 15 as the "Hou" share,
- The next gets 12 as the "Bo" share,
- The next gets 9 as the "Zi" share,
- The lowest gets 6 as the "Nan" share.

Answer: the Gong gets *a* oranges, the Hou gets *b* oranges, the Bo gets *c* oranges, the Zi gets *d* oranges, and the Nan gets *e* oranges.
"""

# 人數別加三顆于下
公 = 15
侯 = 12
伯 = 9
子 = 6
男 = 3

# 副并之，得四十五
副和 = 公 + 侯 + 伯 + 子 + 男

# 以減六十顆
總橘子 = 60
餘橘子 = 總橘子 - 副和

# 餘人數除之，得人三顆
人數 = 5
每人加 = 餘橘子 // 人數

# 各加不并者
a = 公 + 每人加
b = 侯 + 每人加
c = 伯 + 每人加
d = 子 + 每人加
e = 男 + 每人加#----- content ends here -----

"""
"""
