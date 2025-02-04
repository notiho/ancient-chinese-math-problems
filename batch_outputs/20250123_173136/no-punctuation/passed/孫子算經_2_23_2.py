"""
今有五等諸侯共分橘子六十顆人別加三顆問五人各得幾何
術曰先置人數別加三顆于下次六顆次九顆次一十二顆上十五顆副并之得四十五以減六十顆餘人數除之得人三顆各加不并者上得一十八顆為公分次得一十五為侯分次得一十二為伯分次得九為子分下得六為男分
答曰公 a顆 侯 b顆 伯 c顆 子 d顆 男 e顆 
"""

"""
Suppose there are five ranks of nobles sharing 60 oranges, with each person receiving an additional 3 oranges.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people, and add 3 oranges to each rank.
The lowest rank gets 3 oranges, the next gets 6 oranges, the next gets 9 oranges, the next gets 12 oranges, and the highest gets 15 oranges.
Add these together, obtaining 45.
Subtract this from the 60 oranges, leaving the remainder.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add this to the uncombined amounts.
The highest rank gets 18 oranges as the public share, the next gets 15 as the marquis share, the next gets 12 as the earl share, the next gets 9 as the viscount share, and the lowest gets 6 as the baron share.

Answer: The duke gets *a* oranges, the marquis gets *b* oranges, the earl gets *c* oranges, the viscount gets *d* oranges, and the baron gets *e* oranges.
"""

# 橘子總數
橘子總數 = 60

# 各等級加三顆
公加 = 15
侯加 = 12
伯加 = 9
子加 = 6
男加 = 3

# 副并之得四十五
副和 = 公加 + 侯加 + 伯加 + 子加 + 男加

# 減六十顆餘人數除之得人三顆
每人分得 = (橘子總數 - 副和) // 5

# 各加不并者
a = 公加 + 每人分得
b = 侯加 + 每人分得
c = 伯加 + 每人分得
d = 子加 + 每人分得
e = 男加 + 每人分得
"""
"""
