"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters. The eldest daughter returns home every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet at home?

The procedure says: Place the eldest daughter's 5 days, the middle daughter's 4 days, and the youngest daughter's 3 days on the right side.
For each, list one counting rod on the left side.
Multiply them together to find their least common multiple (LCM).
The LCM is the number of days after which all three daughters will meet.

Answer: *a* days.
"""

# 長女五日一歸
長女 = 5

# 中女四日一歸
中女 = 4

# 少女三日一歸
少女 = 3

# 求三數的最小公倍數 (LCM)
def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

# 計算三人的最小公倍數
a = lcm(lcm(長女, 中女), 少女)

# 答案
a#----- content ends here -----

"""
"""
