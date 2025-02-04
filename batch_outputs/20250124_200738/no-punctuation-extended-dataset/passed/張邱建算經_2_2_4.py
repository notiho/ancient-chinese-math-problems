"""
今有馬行轉遲次日減半疾七日行七百里問日行㡬何
術曰置六十四三十二一十六八四二一為差副併為法以行里數乗未併者各自為實實如法而一
答曰初日行 a里 次日行 b里 次日行 c里 次日行 d里 次日行 e里 次日行 f里 次日行 g里
"""

#----- content starts here -----
"""
Suppose there is a horse that slows down each day, halving its speed compared to the previous day.
In seven days, it travels a total of 700 li.
Question: how many li does it travel each day?

The procedure says: Place 64, 32, 16, 8, 4, 2, and 1 as the differences in sequence.
Add them together to form the divisor.
Multiply the total distance (700 li) by each unadded value to form the dividends.
Divide each dividend by the divisor to find the distance traveled each day.

Answer: On the first day, it travels *a* li; on the second day, *b* li; on the third day, *c* li; on the fourth day, *d* li; on the fifth day, *e* li; on the sixth day, *f* li; on the seventh day, *g* li.
"""

# 差副
差副 = [64, 32, 16, 8, 4, 2, 1]

# 副併為法
法 = sum(差副)

# 行里數
行里數 = 700

# 以行里數乘未併者，各自為實
實 = [行里數 * i for i in 差副]

# 實如法而一
a, b, c, d, e, f, g = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
"""
