"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges.
Each person is to receive 3 more oranges than the person below them.
Question: how many oranges does each of the five people receive?

The procedure says: First, place the number of people, each with an additional 3 oranges below them:
Next, 6 oranges, then 9 oranges, then 12 oranges, and finally 15 oranges.
Add these together, obtaining 45.
Subtract this from the total of 60 oranges.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts:
The top receives 18 oranges as the "Gong" share,
The next receives 15 oranges as the "Hou" share,
The next receives 12 oranges as the "Bo" share,
The next receives 9 oranges as the "Zi" share,
The bottom receives 6 oranges as the "Nan" share.

Answer: the Gong receives *a* oranges, the Hou receives *b* oranges, the Bo receives *c* oranges, the Zi receives *d* oranges, and the Nan receives *e* oranges.
"""

# 共分橘子六十顆
橘子總數 = 60

# 先置人數別加三顆于下
人數 = 5
加橘子 = [3 * i for i in range(1, 人數 + 1)]

# 副并之，得四十五
副和 = sum(加橘子)

# 以減六十顆
餘橘子 = 橘子總數 - 副和

# 餘人數除之，得人三顆
每人基數 = 餘橘子 // 人數

# 各加不并者
e = 每人基數 + 加橘子[0]  # 男分
d = 每人基數 + 加橘子[1]  # 子分
c = 每人基數 + 加橘子[2]  # 伯分
b = 每人基數 + 加橘子[3]  # 侯分
a = 每人基數 + 加橘子[4]  # 公分

# 答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""
"""
