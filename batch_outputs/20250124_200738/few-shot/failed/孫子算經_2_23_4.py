"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges. Each person is to receive 3 more oranges than the person below them.
Question: how many oranges does each of the five people receive?

The procedure says: First, place the number of people, each with an additional 3 oranges below them:
Next, 6 oranges, then 9 oranges, then 12 oranges, and finally 15 oranges.
Add these together, obtaining 45.
Subtract this from the total of 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined values:
The top receives 18 oranges as the share for the "Gong" rank.
The next receives 15 as the share for the "Hou" rank.
The next receives 12 as the share for the "Bo" rank.
The next receives 9 as the share for the "Zi" rank.
The bottom receives 6 as the share for the "Nan" rank.

Answer: The "Gong" receives *a* oranges, the "Hou" receives *b* oranges, the "Bo" receives *c* oranges, the "Zi" receives *d* oranges, and the "Nan" receives *e* oranges.
"""

# 總橘子數
橘子總數 = 60

# 每人額外加三顆
額外加數 = 3

# 各等級的基礎橘子數
男 = 6
子 = 9
伯 = 12
侯 = 15
公 = 15 + 額外加數

# 副并之，得四十五
副和 = 男 + 子 + 伯 + 侯 + 公

# 以減六十顆
剩餘橘子 = 橘子總數 - 副和

# 餘人數除之，得人三顆
每人基礎分 = Fraction#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
