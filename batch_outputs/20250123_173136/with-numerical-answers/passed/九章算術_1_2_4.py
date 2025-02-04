"""
今有田廣一里，從一里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a(=15/4)頃 。
"""

"""
Suppose there is a field with a width of 1 li and a length of 1 li.
Question: how large of a field does it make?

The procedure for li fields says: Multiply the numbers of li in width and length with each other, obtaining the [number of] accumulated li.
Multiply it by 375, obtaining the number of mu.

The answer says: *a*(=15/4) qing.
"""

from fractions import Fraction

# 廣一里
廣里數 = 1

# 從一里
從里數 = 1

# 廣從里數相乘得積里
積里 = 廣里數 * 從里數

# 以三百七十五乘之，即畝數
畝數 = 375 * 積里

# 100 畝為 1 頃
a = Fraction(畝數, 100)  # 15/4 qing
"""
"""
