"""
今有環田外周三十步內周一十二步徑三步問為田㡬何
術曰并內外周得四十二步半之得二十一步以徑三步乘之即得
答曰 a步 
"""

"""
Suppose there is an annular (ring-shaped) field. The outer circumference is 30 bu, and the inner circumference is 12 bu. The diameter is 3 bu.
Question: how large is the area of the field?

The procedure says: Add the inner and outer circumferences, obtaining 42 bu.
Halve this, obtaining 21 bu.
Multiply it by the diameter of 3 bu, and the result is the area.

Answer: *a* bu².
"""

# 外周三十步
外周 = 30

# 內周一十二步
內周 = 12

# 徑三步
徑 = 3

# 并內外周得四十二步
周和 = 外周 + 內周

# 半之得二十一步
半周和 = Fraction(周和, 2)

# 以徑三步乘之即得
a = 半周和 * 徑
"""
"""
