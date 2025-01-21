"""
今有五等諸侯共分橘子六十顆人別加三顆問五人各得幾何
術曰先置人數別加三顆于下次六顆次九顆次一十二顆上十五顆副并之得四十五以減六十顆餘人數除之得人三顆各加不并者上得一十八顆為公分次得一十五為侯分次得一十二為伯分次得九為子分下得六為男分
答曰公 a顆 侯 b顆 伯 c顆 子 d顆 男 e顆 
"""

"""
Suppose there are five ranks of nobles sharing 60 oranges. Each person is to receive 3 additional oranges compared to the rank below them.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people, and add 3 oranges for each rank below:
- The bottom rank gets 3 oranges.
- The next rank gets 6 oranges.
- The next rank gets 9 oranges.
- The next rank gets 12 oranges.
- The top rank gets 15 oranges.
Add these together, obtaining 45. Subtract this from 60 oranges, leaving the remainder. Divide the remainder by the number of people, obtaining 3 oranges per person. Add this to the uncombined amounts:
- The top rank gets 18 oranges as the public share.
- The next rank gets 15 oranges as the marquis share.
- The next rank gets 12 oranges as the earl share.
- The next rank gets 9 oranges as the viscount share.
- The bottom rank gets 6 oranges as the baron share.

Answer: The duke gets *a* oranges, the marquis gets *b* oranges, the earl gets *c* oranges, the viscount gets *d* oranges, and the baron gets *e* oranges.
"""

# 橘子總數
橘子總數 = 60

# 各等級基礎分配
男分 = 3
子分 = 6
伯分 = 9
侯分 = 12
公分 = 15

# 副并之得四十五
副和 = 男分 + 子分 + 伯分 + 侯分 + 公分

# 減六十顆餘人數
餘數 = 橘子總數 - 副和

# 餘人數除之得人三顆
人均 = 餘數 // 5

# 各加不并者
e = 男分 + 人均
d = 子分 + 人均
c = 伯分 + 人均
b = 侯分 + 人均
a = 公分 + 人均
"""
"""
