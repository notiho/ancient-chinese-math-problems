"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
術曰：列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a half-wall granary filled with millet. The circumference at the base is 36 chi, and the height is 4 chi and 5 cun.
Question: how much millet does it contain?

The procedure says:
- Take the base circumference of 36 chi and square it, obtaining 1296 square chi.
- Multiply this by the height of 4 chi and 5 cun, obtaining 5832 cubic chi.
- Divide this by 18, obtaining 324 cubic chi.
- Finally, divide by the volume of 1 hu (1 chi 6 cun 2 fen), obtaining the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36  # chi

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert 5 cun to chi (1 chi = 10 cun)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 6 cun 2 fen to chi (1 chi = 10 cun, 1 cun = 10 fen)

# 列下周三十六尺自相乘得一千二百九十六尺
底積 = 下周 ** 2  # Square the circumference

# 以高四尺五寸乘之得五千八百三十二尺
體積 = 底積 * 高  # Multiply by the height

# 以十八除之得三百二十四尺
實體積 = Fraction(體積, 18)  # Divide by 18

# 以斛法一尺六寸二分除之即得
a = Fraction(實體積, 斛法)  # Divide by the volume of 1 hu

# Output the result
a#----- content ends here -----

"""
"""
