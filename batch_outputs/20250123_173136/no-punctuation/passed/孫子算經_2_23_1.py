"""
今有五等諸侯共分橘子六十顆人別加三顆問五人各得幾何
術曰先置人數別加三顆于下次六顆次九顆次一十二顆上十五顆副并之得四十五以減六十顆餘人數除之得人三顆各加不并者上得一十八顆為公分次得一十五為侯分次得一十二為伯分次得九為子分下得六為男分
答曰公 a顆 侯 b顆 伯 c顆 子 d顆 男 e顆 
"""

"""
Suppose there are five ranks of nobles sharing 60 oranges. Each person is to receive 3 extra oranges compared to the rank below them.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people, and add 3 oranges for each rank below:
- The lowest rank gets 3 oranges.
- The next rank gets 6 oranges.
- The next rank gets 9 oranges.
- The next rank gets 12 oranges.
- The highest rank gets 15 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts:
- The highest rank receives 18 oranges as the public share.
- The next rank receives 15 oranges as the marquis share.
- The next rank receives 12 oranges as the earl share.
- The next rank receives 9 oranges as the viscount share.
- The lowest rank receives 6 oranges as the baron share.

Answer: The duke gets *a* oranges, the marquis gets *b* oranges, the earl gets *c* oranges, the viscount gets *d* oranges, and the baron gets *e* oranges.
"""

# 各等級加三顆
加三顆 = 3

# 各等級的橘子數量
男 = 加三顆
子 = 男 + 加三顆
伯 = 子 + 加三顆
侯 = 伯 + 加三顆
公 = 侯 + 加三顆

# 副并之得四十五
副和 = 男 + 子 + 伯 + 侯 + 公

# 以減六十顆
總橘子 = 60
餘數 = 總橘子 - 副和

# 餘人數除之得人三顆
人均 = Fraction(餘數, 5)

# 各加不并者
a = 公 + 人均
b = 侯 + 人均
c = 伯 + 人均
d = 子 + 人均
e = 男 + 人均
"""
"""
