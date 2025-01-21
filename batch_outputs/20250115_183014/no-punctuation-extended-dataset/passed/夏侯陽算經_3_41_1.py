"""
今有兵三千四百八十五人毎人賜絹一丈三尺問絹幾何
術曰先置人數添三得丈數以四為法除之得匹
答曰 a匹 b丈
"""

"""
Suppose there are 3485 soldiers, and each soldier is rewarded with 1 zhang and 3 chi of silk.
Question: how much silk is needed in total?

The procedure says: First, place the number of people. Add 3 [chi] to get the total zhang.
Divide by 4 (since 1 bolt of silk equals 4 zhang) to get the number of bolts.

Answer: *a* bolts and *b* zhang.
"""

from fractions import Fraction

# 兵三千四百八十五人
兵數 = 3485

# 每人賜絹一丈三尺
每人絹 = 1 + Fraction(3, 10)  # 1丈3尺 = 1 + 3/10丈

# 先置人數添三得丈數
總丈數 = 兵數 * 每人絹

# 以四為法除之得匹
法 = 4  # 1匹 = 4丈
匹數 = int(總丈數 // 法)  # 整數部分為匹數
剩餘丈數 = 總丈數 % 法  # 餘數為剩餘的丈數

a = 匹數
b = 剩餘丈數
"""
"""
