"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a(=18)顆 ，侯 b(=15)顆 ，伯 c(=12)顆 ，子 d(=9)顆 ，男 e(=6)顆 。
"""

"""
Suppose there are five ranks of feudal lords, who together divide 60 oranges. Each person is given an additional 3 oranges.
Question: how many does each of the five people receive?

The procedure says: First, place the number of people, each with an additional 3 oranges below:
Next, 6 oranges, then 9 oranges, then 12 oranges, and finally 15 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Each person is then given their additional oranges (not combined with the remainder):
The top receives 18 oranges as the "Gong" share, the next receives 15 as the "Hou" share, the next receives 12 as the "Bo" share, the next receives 9 as the "Zi" share, and the bottom receives 6 as the "Nan" share.

Answer: The Gong receives *a*(=18) oranges, the Hou receives *b*(=15) oranges, the Bo receives *c*(=12) oranges, the Zi receives *d*(=9) oranges, and the Nan receives *e*(=6) oranges.
"""

# 五等諸侯
人數 = 5

# 各人別加三顆
加橘 = 3

# 各人額外橘子數
橘子數 = [6, 9, 12, 15, 18]

# 副并之，得四十五
副和 = sum(橘子數)

# 以減六十顆
總橘子 = 60
餘橘子 = 總橘子 - 副和

# 餘人數除之，得人三顆
每人橘子 = 餘橘子 // 人數

# 各加不并者
a = 橘子數[4] + 每人橘子  # 公得 18 顆
b = 橘子數[3] + 每人橘子  # 侯得 15 顆
c = 橘子數[2] + 每人橘子  # 伯得 12 顆
d = 橘子數[1] + 每人橘子  # 子得 9 顆
e = 橘子數[0] + 每人橘子  # 男得 6 顆
"""
"""
