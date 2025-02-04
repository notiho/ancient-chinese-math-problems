"""
今有半壁聚粟下周三十六尺高四尺五寸問粟㡬何
術曰列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a half-walled granary with a base circumference of 36 chi and a height of 4 chi 5 cun.
Question: how much millet does it contain?

The procedure says: Place the base circumference of 36 chi, multiply it by itself, obtaining 1296 chi².
Multiply this by the height of 4 chi 5 cun, obtaining 5832 chi³.
Divide this by 18, obtaining 324 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen, and the result is the amount of millet.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # 5 寸 = 5/10 尺

# 列下周三十六尺，自相乘
積1 = 下周 * 下周  # 得 1296 尺²

# 以高四尺五寸乘之
積2 = 積1 * 高  # 得 5832 尺³

# 以十八除之
積3 = Fraction(積2, 18)  # 得 324 尺³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1 尺 6 寸 2 分 = 1 + 6/10 + 2/100 尺

# 以斛法除之，即得
a = Fraction(積3, 斛法)  # 得斛數

a
"""
"""
