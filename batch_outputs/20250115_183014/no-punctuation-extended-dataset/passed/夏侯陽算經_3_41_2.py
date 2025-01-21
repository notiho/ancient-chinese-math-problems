"""
今有兵三千四百八十五人毎人賜絹一丈三尺問絹幾何
術曰先置人數添三得丈數以四為法除之得匹
答曰 a匹 b丈
"""

"""
Suppose there are 3485 soldiers, and each soldier is rewarded with 1 zhang and 3 chi of silk.
Question: how much silk is needed in total?

The procedure says: First, place the number of people.
Add 3 [chi] to obtain the total zhang.
Divide by 4 (since 1 bolt of silk = 4 zhang) to obtain the number of bolts.

Answer: *a* bolts and *b* zhang.
"""

# 兵三千四百八十五人
人數 = 3485

# 每人賜絹一丈三尺
每人絹丈數 = 1
每人絹尺數 = 3

# 先置人數添三得丈數
總丈數 = 人數 * 每人絹丈數 + Fraction(人數 * 每人絹尺數, 10)

# 以四為法除之得匹
法 = 4
匹數 = Fraction(總丈數, 法)

# 分解為整匹和剩餘丈數
a = 匹數.numerator // 匹數.denominator  # 整匹數
b = 匹數 - a  # 剩餘丈數

b = b * 法  # 將剩餘部分轉回丈數

"""
"""
