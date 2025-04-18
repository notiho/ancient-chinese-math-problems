"""
又有環田中周六十二步四分步之三外周一百一十三步二分步之一徑十二步三分步之二問為田幾何
術曰并中外周而半之以徑乘之為積步
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a circular field.
The inner circumference is 62 bu and 3/4 bu.
The outer circumference is 113 bu and 1/2 bu.
The diameter is 12 bu and 2/3 bu.
Question: how large is the field?

The procedure says: Add the inner and outer circumferences, then halve the result.
Multiply this by the diameter to obtain the accumulated bu.

The answer says: *a* mu.
"""

from fractions import Fraction

# 中周六十二步四分步之三
中周 = 62 + Fraction(3, 4)

# 外周一百一十三步二分步之一
外周 = 113 + Fraction(1, 2)

# 徑十二步三分步之二
徑 = 12 + Fraction(2, 3)

# 并中外周而半之
平均周 = (中周 + 外周) / 2

# 以徑乘之，為積步
積步 = 平均周 * 徑

# 畝法二百四十步
畝法 = 240

# 以畝法二百四十步除之，即畝數
a = Fraction(積步, 畝法)#----- content ends here -----

"""
"""
