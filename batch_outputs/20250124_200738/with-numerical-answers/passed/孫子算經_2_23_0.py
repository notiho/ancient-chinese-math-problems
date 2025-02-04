"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a(=18)顆 ，侯 b(=15)顆 ，伯 c(=12)顆 ，子 d(=9)顆 ，男 e(=6)顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges.
Each person is to receive 3 additional oranges compared to the rank below them.
Question: how many oranges does each of the five people receive?

The procedure says: First, place the number of people, adding 3 oranges for each rank below.
Then, place 6 oranges, then 9 oranges, then 12 oranges, and finally 15 oranges.
Add these together, obtaining 45.
Subtract this from the total of 60 oranges.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts.
The top rank receives 18 oranges as the "Gong" share, the next receives 15 as the "Hou" share, the next receives 12 as the "Bo" share, the next receives 9 as the "Zi" share, and the last receives 6 as the "Nan" share.

Answer: The "Gong" receives *a*(=18) oranges, the "Hou" receives *b*(=15) oranges, the "Bo" receives *c*(=12) oranges, the "Zi" receives *d*(=9) oranges, and the "Nan" receives *e*(=6) oranges.
"""

# 人數別加三顆于下
加橘數 = [3, 6, 9, 12, 15]

# 副并之，得四十五
副和 = sum(加橘數)  # 45

# 以減六十顆
總橘數 = 60
餘橘數 = 總橘數 - 副和  # 15

# 餘人數除之，得人三顆
人數 = 5
每人基數 = 餘橘數 // 人數  # 3

# 各加不并者
a = 加橘數[4] + 每人基數  # 18
b = 加橘數[3] + 每人基數  # 15
c = 加橘數[2] + 每人基數  # 12
d = 加橘數[1] + 每人基數  # 9
e = 加橘數[0] + 每人基數  # 6#----- content ends here -----

"""
"""
