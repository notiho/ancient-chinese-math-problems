"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, who are to divide 60 oranges. Each person is to receive an additional 3 oranges compared to the rank below them.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people and add 3 oranges for each rank below:
- The lowest rank gets 3 oranges,
- The next rank gets 6 oranges,
- The next rank gets 9 oranges,
- The next rank gets 12 oranges,
- The highest rank gets 15 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder. Divide the remainder by the number of people, obtaining 3 oranges per person. Add this to the uncombined amounts:
- The highest rank gets 18 oranges as the "gong" share,
- The next rank gets 15 oranges as the "hou" share,
- The next rank gets 12 oranges as the "bo" share,
- The next rank gets 9 oranges as the "zi" share,
- The lowest rank gets 6 oranges as the "nan" share.

Answer: the "gong" gets *a* oranges, the "hou" gets *b* oranges, the "bo" gets *c* oranges, the "zi" gets *d* oranges, and the "nan" gets *e* oranges.
"""

# 橘子總數
橘子總數 = 60

# 各等級加三顆
男 = 3
子 = 6
伯 = 9
侯 = 12
公 = 15

# 副并之，得四十五
副和 = 男 + 子 + 伯 + 侯 + 公

# 以減六十顆
餘數 = 橘子總數 - 副和

# 餘人數除之，得人三顆
每人加 = 餘數 // 5

# 各加不并者
e = 男 + 每人加
d = 子 + 每人加
c = 伯 + 每人加
b = 侯 + 每人加
a = 公 + 每人加#----- content ends here -----

"""
"""
