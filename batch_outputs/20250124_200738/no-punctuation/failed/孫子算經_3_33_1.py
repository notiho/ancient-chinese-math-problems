"""
今有三女長女五日一歸中女四日一歸少女三日一歸問三女幾何日相會
術曰置長女五日中女四日少女三日于右方各列一算于左方維乘之各得所到數長女十二到中女十五到少女二十到又各以歸日乘到數即得
答曰 a日 
"""

#----- content starts here -----
"""
Suppose there are three women: the eldest returns home every 5 days, the middle one every 4 days, and the youngest every 3 days.
Question: after how many days will all three meet at home?

The procedure says: Place the eldest's 5 days, the middle's 4 days, and the youngest's 3 days on the right side, each as a single counting rod.
On the left side, multiply them together, obtaining the least common multiple.
For the eldest, multiply her return days by the product of the other two's days.
For the middle, multiply her return days by the product of the other two's days.
For the youngest, multiply her return days by the product of the other two's days.
Add these products together, and divide by the least common multiple to find the answer.

Answer: *a* days.
"""

# 長女五日
長女 = 5

# 中女四日
中女 = 4

# 少女三日
少女 = 3

# 維乘之，得最小公倍數
最小公倍數 = 長女 * 中女 * 少女

# 長女十二到 (中女 * 少女)
長女到 = 中女 * 少女

# 中女十五到 (長女 * 少女)
中女到 = 長女 * 少女

# 少女二十到 (長女 * 中女)
少女到 = 長女 * 中女

# 各以歸日乘到數
長女積 = 長女 * 長女到
中女積 = 中女 * 中女到
少女積 = 少女 * 少女到

# 加起來，並以最小公倍數除之
a = Fraction(長女積 + 中女積 + 少女積, 最小公倍數)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60, Actual: 3"""
