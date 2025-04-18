"""
今有環田，中周九十二步，外周一百二十二步，徑五步。問：為田幾何？
術曰：并中外周而半之，以徑乘之為積步。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a circular field. The inner circumference is 92 bu, and the outer circumference is 122 bu. The diameter is 5 bu.
Question: how large is the field in mu?

The procedure says: Add the inner and outer circumferences, then halve the sum. Multiply this by the diameter to obtain the total area in bu².
Finally, divide by 240 (the mu divisor) to convert to mu.

Answer: *a* mu.
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

# 以畝法除之，即畝數
a = Fraction(積步, 畝法)

a#----- content ends here -----

"""
"""
