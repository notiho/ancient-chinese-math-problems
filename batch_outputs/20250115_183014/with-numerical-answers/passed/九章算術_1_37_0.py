"""
又有環田，中周六十二步、四分步之三，外周一百一十三步、二分步之一，徑十二步、三分步之二。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a(=893/192)畝 。
"""

"""
Suppose there is a circular field. The inner circumference is 62 bu and 3/4 bu, the outer circumference is 113 bu and 1/2 bu, and the diameter is 12 bu and 2/3 bu.
Question: how large is the field?

The procedure says: Add the inner and outer circumferences, then halve the sum. Multiply it by the diameter to obtain the accumulated bu.

The answer says: *a*(=893/192) mu.
"""

from fractions import Fraction

# 中周六十二步、四分步之三
中周 = 62 + Fraction(3, 4)

# 外周一百一十三步、二分步之一
外周 = 113 + Fraction(1, 2)

# 并中外周而半之
平均周 = (中周 + 外周) / 2

# 徑十二步、三分步之二
徑 = 12 + Fraction(2, 3)

# 以徑乘之為積步
積步 = 平均周 * 徑

# 畝法二百四十步
畝法 = 240

# 積步除以畝法，得畝數
a = Fraction(積步, 畝法) # 893/192
"""
"""
