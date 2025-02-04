"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a(=18)顆 ，侯 b(=15)顆 ，伯 c(=12)顆 ，子 d(=9)顆 ，男 e(=6)顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges. Each person is to receive 3 more oranges than the one below them.
Question: how many does each of the five people receive?

The procedure says: First, place the number of people, adding 3 oranges for each rank below:
- The lowest gets 3 oranges,
- The next gets 6 oranges,
- The next gets 9 oranges,
- The next gets 12 oranges,
- The highest gets 15 oranges.
Add these together, obtaining 45. Subtract this from the total of 60 oranges, leaving the remainder. Divide the remainder by the number of people, obtaining 3 oranges per person. Add this to the uncombined amounts:
- The highest gets 18 oranges as the "Gong" share,
- The next gets 15 as the "Hou" share,
- The next gets 12 as the "Bo" share,
- The next gets 9 as the "Zi" share,
- The lowest gets 6 as the "Nan" share.

Answer: The "Gong" gets *a*(=18) oranges, the "Hou" gets *b*(=15) oranges, the "Bo" gets *c*(=12) oranges, the "Zi" gets *d*(=9) oranges, and the "Nan" gets *e*(=6) oranges.
"""

# 人別加三顆于下
加數 = [3, 6, 9, 12, 15]

# 副并之，得四十五
副和 = sum(加數)

# 以減六十顆
總橘子 = 60
餘數 = 總橘子 - 副和

# 餘人數除之，得人三顆
人數 = 5
每人加 = 餘數 // 人數

# 各加不并者
a = 加數[4] + 每人加  # 18
b = 加數[3] + 每人加  # 15
c = 加數[2] + 每人加  # 12
d = 加數[1] + 每人加  # 9
e = 加數[0] + 每人加  # 6#----- content ends here -----

"""
"""
