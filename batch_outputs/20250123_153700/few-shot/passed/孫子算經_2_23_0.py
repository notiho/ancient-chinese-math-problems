"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges.
Each person is to receive 3 more oranges than the one below them.
Question: how many does each of the five people receive?

The procedure says: First, place the number of people, each adding 3 oranges below.
Then 6 oranges, then 9 oranges, then 12 oranges, and finally 15 oranges.
Add these together, obtaining 45.
Subtract this from 60 oranges, and divide the remainder by the number of people, obtaining 3 oranges per person.
Each adds the uncombined amounts.
The top receives 18 oranges as the duke's share, the next receives 15 as the marquis's share, the next receives 12 as the earl's share, the next receives 9 as the viscount's share, and the bottom receives 6 as the baron's share.

Answer: the duke receives *a* oranges, the marquis receives *b* oranges, the earl receives *c* oranges, the viscount receives *d* oranges, and the baron receives *e* oranges.
"""

# 總橘子數
總橘子 = 60

# 各人額外加的橘子數
加橘子 = [3, 6, 9, 12, 15]

# 副并之，得四十五
副和 = sum(加橘子)

# 以減六十顆
餘橘子 = 總橘子 - 副和

# 餘人數除之，得人三顆
人數 = 5
每人基數 = Fraction(餘橘子, 人數)

# 各加不并者
e = 每人基數 + 加橘子[0]  # 男分
d = 每人基數 + 加橘子[1]  # 子分
c = 每人基數 + 加橘子[2]  # 伯分
b = 每人基數 + 加橘子[3]  # 侯分
a = 每人基數 + 加橘子[4]  # 公分
"""
"""
