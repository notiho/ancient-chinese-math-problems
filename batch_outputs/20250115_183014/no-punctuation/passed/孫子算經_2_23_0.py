"""
今有五等諸侯共分橘子六十顆人別加三顆問五人各得幾何
術曰先置人數別加三顆于下次六顆次九顆次一十二顆上十五顆副并之得四十五以減六十顆餘人數除之得人三顆各加不并者上得一十八顆為公分次得一十五為侯分次得一十二為伯分次得九為子分下得六為男分
答曰公 a顆 侯 b顆 伯 c顆 子 d顆 男 e顆 
"""

"""
Suppose there are five ranks of nobles sharing 60 oranges. Each person gets 3 additional oranges compared to the next rank below.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people, adding 3 oranges for each rank below.
The lowest rank gets 3, the next gets 6, the next gets 9, the next gets 12, and the highest gets 15.
Add these together, obtaining 45. Subtract this from 60, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts:
- The highest rank gets 18 oranges as the public share.
- The next gets 15 as the marquis share.
- The next gets 12 as the earl share.
- The next gets 9 as the viscount share.
- The lowest gets 6 as the baron share.

Answer: The duke (公) gets *a* oranges, the marquis (侯) gets *b* oranges, the earl (伯) gets *c* oranges, the viscount (子) gets *d* oranges, and the baron (男) gets *e* oranges.
"""

# 橘子總數
橘子總數 = 60

# 各等級加的橘子數
男 = 3
子 = 6
伯 = 9
侯 = 12
公 = 15

# 副并之得四十五
副和 = 男 + 子 + 伯 + 侯 + 公

# 以減六十顆，餘人數除之，得人三顆
每人分得 = (橘子總數 - 副和) // 5

# 各加不并者
a = 公 + 每人分得
b = 侯 + 每人分得
c = 伯 + 每人分得
d = 子 + 每人分得
e = 男 + 每人分得
"""
"""
