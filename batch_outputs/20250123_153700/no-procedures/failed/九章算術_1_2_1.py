"""
今有田廣一里，從一里。問：為田幾何？
荅曰： a頃 。
"""

"""
Suppose there is a field with a width of 1 li and a length of 1 li.
Question: how large is the field?

Answer: it makes *a* qing.
"""

# 廣一里
廣 = 1  # in li

# 從一里
從 = 1  # in li

# 1 li × 1 li = 1 square li
田_in_square_li = 廣 * 從

# 1 square li = 100 mu = 1 qing
a = 田_in_square_li  # since 1 square li is exactly 1 qing

a  # Output the result in qing
"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 1"""
