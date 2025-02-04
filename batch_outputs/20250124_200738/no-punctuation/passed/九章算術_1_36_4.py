"""
今有環田中周九十二步外周一百二十二步徑五步問為田幾何
術曰并中外周而半之以徑乘之為積步
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a circular field with an inner circumference of 92 bu, an outer circumference of 122 bu, and a diameter of 5 bu.
Question: how large is the field?

The procedure says: Add the inner and outer circumferences, then halve the sum.
Multiply this by the diameter to obtain the accumulated bu.
Divide the accumulated bu by the mu-divisor, 240, to obtain the number of mu.

The answer says: *a* mu.
"""

# 中周九十二步
中周 = 92

# 外周一百二十二步
外周 = 122

# 徑五步
徑 = 5

# 并中外周而半之
平均周 = Fraction((中周 + 外周), 2)

# 以徑乘之，為積步
積步 = 平均周 * 徑

# 畝法二百四十步
畝法 = 240

# 以畝法除之，即畝數
a = Fraction(積步, 畝法)#----- content ends here -----

"""
"""
