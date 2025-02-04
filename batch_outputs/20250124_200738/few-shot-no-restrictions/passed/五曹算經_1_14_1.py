"""
今有覆月田從三十步徑十步。問：為田㡬何？
術曰：列徑十步半之得五步以從三十步乘之即得。
答曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 30 bu and a diameter of 10 bu.
Question: how large is the area of the field?

The procedure says: Take the diameter of 10 bu, halve it to obtain 5 bu. Multiply this by the circumference of 30 bu to obtain the area.

Answer: *a* bu².
"""

from fractions import Fraction

# 徑十步
徑 = 10

# 半之得五步
半徑 = Fraction(徑, 2)

# 從三十步
從 = 30

# 以從三十步乘之即得
a = 半徑 * 從

# Output the result
a#----- content ends here -----

"""
"""
