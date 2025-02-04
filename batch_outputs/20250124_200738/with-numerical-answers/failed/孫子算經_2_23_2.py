"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a(=18)顆 ，侯 b(=15)顆 ，伯 c(=12)顆 ，子 d(=9)顆 ，男 e(=6)顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of nobles, and they are to divide 60 oranges.
Each person receives an additional 3 oranges based on their rank.
Question: how many does each of the five receive?

The procedure says: First, place the number of people, adding 3 oranges for each rank.
Next, place 6 oranges, then 9 oranges, then 12 oranges, and finally 15 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts.
The top receives 18 oranges as the share for the Gong rank, the next receives 15 as the share for the Hou rank, the next receives 12 as the share for the Bo rank, the next receives 9 as the share for the Zi rank, and the bottom receives 6 as the share for the Nan rank.

Answer: The Gong receives *a*(=18) oranges, the Hou receives *b*(=15) oranges, the Bo receives *c*(=12) oranges, the Zi receives *d*(=9) oranges, and the Nan receives *e*(=6) oranges.
"""

# 人別加三顆于下
加三 = 3

# 次六顆，次九顆，次一十二顆，上十五顆
分配 = [6, 9, 12, 15, 18]

# 副并之，得四十五
副和 = sum分配 = sum分配 = sum(分配)#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
