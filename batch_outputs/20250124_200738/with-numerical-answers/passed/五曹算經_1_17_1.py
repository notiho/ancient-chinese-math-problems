"""
今有環田外周三十步內周一十二步徑三步。問：為田㡬何？
術曰：并內外周得四十二步半之得二十一步以徑三步乘之即得。
答曰： a(=63)步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with an outer circumference of 30 bu, an inner circumference of 12 bu, and a diameter of 3 bu.
Question: how large is the field?

The procedure says: Add the inner and outer circumferences, obtaining 42 bu.
Take half of this, obtaining 21 bu.
Multiply it by the diameter of 3 bu, and the result is the area.

Answer: *a*(=63) bu².
"""

# 外周三十步
外周 = 30

# 內周一十二步
內周 = 12

# 徑三步
徑 = 3

# 并內外周得四十二步
總周 = 外周 + 內周

# 半之得二十一步
半周 = Fraction(總周, 2)

# 以徑三步乘之即得
a = 半周 * 徑 # 63#----- content ends here -----

"""
"""
