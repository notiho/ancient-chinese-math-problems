"""
今有三女長女五日一歸中女四日一歸少女三日一歸問三女幾何日相會
術曰置長女五日中女四日少女三日于右方各列一算于左方維乘之各得所到數長女十二到中女十五到少女二十到又各以歸日乘到數即得
答曰 a日 
"""

"""
Suppose there are three women: the eldest daughter returns every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side, each listed as one count.
On the left side, multiply them together, obtaining the numbers they reach.
The eldest daughter reaches 12, the middle daughter 15, and the youngest daughter 20.
Then, multiply each by their respective return days, obtaining the result.

Answer: *a* days.
"""

# 長女五日
長女 = 5

# 中女四日
中女 = 4

# 少女三日
少女 = 3

# 各列一算，維乘之
到數 = 長女 * 中女 * 少女

# 長女十二到，中女十五到，少女二十到
長女到 = 到數 // 長女
中女到 = 到數 // 中女
少女到 = 到數 // 少女

# 又各以歸日乘到數，即得
長女歸 = 長女到 * 長女
中女歸 = 中女到 * 中女
少女歸 = 少女到 * 少女

# 最小公倍數即為相會日
a = Fraction(到數, 1)  # The least common multiple is the product divided by the greatest common divisor, but here it's already encoded in 到數.
"""
"""
