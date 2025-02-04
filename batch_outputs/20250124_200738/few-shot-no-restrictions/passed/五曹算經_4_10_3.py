"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
術曰：列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a half-wall granary filled with millet. Its base circumference is 36 chi, and its height is 4 chi and 5 cun.
Question: how much millet does it hold?

The procedure says: Take the base circumference of 36 chi, multiply it by itself, obtaining 1296 chi².
Multiply this by the height of 4 chi and 5 cun, obtaining 5832 chi³.
Divide this by 18, obtaining 324 chi³.
Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen), obtaining the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36  # chi

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # 4 chi and 5 cun (1 chi = 10 cun)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen

# 列下周三十六尺自相乘
底積 = 下周 * 下周  # chi²

# 以高四尺五寸乘之
體積 = 底積 * 高  # chi³

# 以十八除之
體積 = Fraction(體積, 18)  # chi³

# 以斛法一尺六寸二分除之即得
a = Fraction(體積, 斛法)  # hu

a#----- content ends here -----

"""
"""
