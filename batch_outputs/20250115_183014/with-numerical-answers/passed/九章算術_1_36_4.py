"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a(=107/48)畝 。
"""

"""
Suppose there is a circular field. The inner circumference is 92 bu, and the outer circumference is 122 bu. The diameter is 5 bu.
Question: how large is the field?

The procedure says: Add the inner and outer circumferences together and halve them. Multiply this by the diameter to obtain the accumulated bu.

The answer says: *a*(=107/48) mu.
"""

from fractions import Fraction

# 中周九十二步
中周 = 92

# 外周一百二十二步
外周 = 122

# 徑五步
徑 = 5

# 并中外周而半之
平均周 = Fraction(中周 + 外周, 2)

# 以徑乘之為積步
積步 = 平均周 * 徑

# 畝法二百四十步
畝法 = 240

# 積步除以畝法得畝數
a = Fraction(積步, 畝法)  # 107/48

"""
"""
