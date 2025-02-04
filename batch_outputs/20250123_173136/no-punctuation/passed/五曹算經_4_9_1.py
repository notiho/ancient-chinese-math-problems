"""
今有內角聚粟下周五十四尺高五尺問粟㡬何
術曰列下周五十四尺自相乘得二千九百一十六尺以高五尺乘之得一萬四千五百八十尺以九除之得一千六百二十尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a granary with an inner circular base circumference of 54 chi and a height of 5 chi.
Question: how much millet can it hold?

The procedure says: Take the base circumference of 54 chi and multiply it by itself, obtaining 2916 chi².
Multiply this by the height of 5 chi, obtaining 14580 chi³.
Divide this by 9, obtaining 1620 chi³.
Divide this by the hu-divisor, which is 1 chi 6 cun 2 fen (1.62 chi), to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周五十四尺
下周 = 54

# 高五尺
高 = 5

# 列下周五十四尺，自相乘
底積 = 下周 * 下周  # 得 2916 尺²

# 以高五尺乘之
體積 = 底積 * 高  # 得 14580 尺³

# 以九除之
體積除九 = Fraction(體積, 9)  # 得 1620 尺³

# 斛法一尺六寸二分 (1.62 尺)
斛法 = Fraction(162, 100)  # 1.62 尺

# 以斛法除之，即得
a = Fraction(體積除九, 斛法)  # 結果為斛數
"""
"""
