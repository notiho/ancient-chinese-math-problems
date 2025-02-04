"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
術曰：列下周五十四尺自相乘得二千九百一十六尺以高五尺乘之得一萬四千五百八十尺以九除之得一千六百二十尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a granary with a circular base. The circumference of the base is 54 chi, and the height is 5 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of the base (54 chi), square it to get 2916 chi².
Multiply this by the height (5 chi) to get 14580 chi³.
Divide this by 9 to account for the shape of the granary, obtaining 1620 chi³.
Finally, divide this by the volume of 1 hu (1 chi³ = 1.62 hu) to get the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周五十四尺
下周 = 54  # chi

# 高五尺
高 = 5  # chi

# 列下周五十四尺自相乘
底積 = 下周 ** 2  # chi²

# 以高五尺乘之
體積 = 底積 * 高  # chi³

# 以九除之
體積調整 = Fraction(體積, 9)  # chi³

# 斛法一尺六寸二分 (1 chi³ = 1.62 hu)
斛法 = Fraction(162, 100)  # 1.62 hu

# 以斛法除之
a = Fraction(體積調整, 斛法)

# Output the result
a#----- content ends here -----

"""
"""
