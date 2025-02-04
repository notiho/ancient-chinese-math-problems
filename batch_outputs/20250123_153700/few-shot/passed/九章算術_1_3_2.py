"""
又有田廣二里，從三里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

"""
Suppose there is a field with a width of 2 li and a length of 3 li.
Question: how large of a field does it make?

The procedure for li fields says: Multiply the width and length in li, obtaining the accumulated li.
Multiply it by 375, obtaining the number of mu.

The answer says: *a* qing.
"""

# 廣二里
廣里數 = 2

# 從三里
從里數 = 3

# 廣從里數相乘得積里
積里 = 廣里數 * 從里數

# 以三百七十五乘之，即畝數
畝數 = 375 * 積里

# 100 畝為 1 頃
a = Fraction(畝數, 100)
"""
"""
