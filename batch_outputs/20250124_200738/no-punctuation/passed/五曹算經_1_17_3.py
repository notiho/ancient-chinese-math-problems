"""
今有環田外周三十步內周一十二步徑三步問為田㡬何
術曰并內外周得四十二步半之得二十一步以徑三步乘之即得
答曰 a步 
"""

#----- content starts here -----
"""
Suppose there is an annular field (a ring-shaped field) with an outer circumference of 30 bu and an inner circumference of 12 bu. The diameter is 3 bu.
Question: how large is the field?

The procedure says: Add the inner and outer circumferences, obtaining 42 bu.
Halve this, obtaining 21 bu.
Multiply it by the diameter, 3 bu, and the result is the area.

Answer: *a* bu².
"""

# 外周三十步
外周 = 30

# 內周一十二步
內周 = 12

# 并內外周，得四十二步
總周 = 外周 + 內周

# 半之，得二十一步
半周 = Fraction(總周, 2)

# 徑三步
徑 = 3

# 以徑三步乘之，即得
a = 半周 * 徑#----- content ends here -----

"""
"""
