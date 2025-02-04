"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
術曰：列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a semicircular wall storing millet. The circumference of the base is 36 chi, and the height is 4 chi and 5 cun.
Question: how much millet does it hold?

The procedure says: Take the circumference of the base, 36 chi, and square it, obtaining 1296 chi².
Multiply this by the height, 4 chi and 5 cun, obtaining 5832 chi³.
Divide this by 18, obtaining 324 chi³.
Finally, divide this by the volume conversion factor, 1 chi 6 cun 2 fen (1.62 chi), to obtain the volume in hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36  # chi

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # 4 chi and 5 cun (1 cun = 1/10 chi)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen (1 cun = 1/10 chi, 1 fen = 1/100 chi)

# 列下周三十六尺自相乘
積1 = 下周 ** 2  # chi²

# 以高四尺五寸乘之
積2 = 積1 * 高  # chi³

# 以十八除之
積3 = Fraction(積2, 18)  # chi³

# 以斛法一尺六寸二分除之即得
a = Fraction(積3, 斛法)  # hu

a#----- content ends here -----

"""
"""
