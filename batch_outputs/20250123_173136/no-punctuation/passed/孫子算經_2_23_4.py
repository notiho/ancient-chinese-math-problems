"""
今有五等諸侯共分橘子六十顆人別加三顆問五人各得幾何
術曰先置人數別加三顆于下次六顆次九顆次一十二顆上十五顆副并之得四十五以減六十顆餘人數除之得人三顆各加不并者上得一十八顆為公分次得一十五為侯分次得一十二為伯分次得九為子分下得六為男分
答曰公 a顆 侯 b顆 伯 c顆 子 d顆 男 e顆 
"""

"""
Suppose there are five ranks of nobles sharing 60 oranges. Each person is to receive 3 additional oranges compared to the next rank.
Question: how many oranges does each of the five ranks receive?

The procedure says: First, place the number of people, and add 3 oranges for each rank below:
- Add 3 oranges for the lowest rank,
- Add 6 oranges for the next rank,
- Add 9 oranges for the next rank,
- Add 12 oranges for the next rank,
- Add 15 oranges for the highest rank.
Sum these additional oranges, obtaining 45. Subtract this from the total of 60 oranges, leaving the number of people.
Divide the remainder by the number of people, obtaining 3 oranges per person.
Add the uncombined additional oranges to this base amount:
- The highest rank receives 18 oranges,
- The next rank receives 15 oranges,
- The next rank receives 12 oranges,
- The next rank receives 9 oranges,
- The lowest rank receives 6 oranges.

Answer: The duke receives *a* oranges, the marquis receives *b* oranges, the earl receives *c* oranges, the viscount receives *d* oranges, and the baron receives *e* oranges.
"""

# 橘子總數
橘子總數 = 60

# 各等級的額外橘子數
男額外 = 3
子額外 = 6
伯額外 = 9
侯額外 = 12
公額外 = 15

# 副并之得四十五
總額外 = 男額外 + 子額外 + 伯額外 + 侯額外 + 公額外

# 以減六十顆
剩餘橘子 = 橘子總數 - 總額外

# 餘人數除之得人三顆
基礎橘子 = 剩餘橘子 // 5

# 各加不并者
e = 基礎橘子 + 男額外  # 男分
d = 基礎橘子 + 子額外  # 子分
c = 基礎橘子 + 伯額外  # 伯分
b = 基礎橘子 + 侯額外  # 侯分
a = 基礎橘子 + 公額外  # 公分
"""
"""
