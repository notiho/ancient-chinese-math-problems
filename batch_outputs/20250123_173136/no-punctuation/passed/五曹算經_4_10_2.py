"""
今有半壁聚粟下周三十六尺高四尺五寸問粟㡬何
術曰列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a half-walled granary filled with millet. The base circumference is 36 chi, and the height is 4 chi and 5 cun.
Question: how much millet does it hold?

The procedure says: Take the base circumference of 36 chi, multiply it by itself, obtaining 1296 chi².
Multiply this by the height of 4 chi and 5 cun, obtaining 5832 chi³.
Divide this by 18, obtaining 324 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen, obtaining the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36

# 高四尺五寸
高 = 4 + Fraction(5, 10)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)

# 列下周三十六尺，自相乘
積 = 下周 * 下周

# 以高四尺五寸乘之
積 = 積 * 高

# 以十八除之
積 = Fraction(積, 18)

# 以斛法一尺六寸二分除之，即得
a = Fraction(積, 斛法)
"""
"""
