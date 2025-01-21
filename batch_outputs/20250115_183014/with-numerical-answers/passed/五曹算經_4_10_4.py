"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
術曰：列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得。
答曰： a(=200)斛 。
"""

"""
Suppose there is a half-wall granary with a base circumference of 36 chi and a height of 4 chi 5 cun.
Question: how much millet does it hold?

The procedure says: Place the base circumference of 36 chi, multiply it by itself, obtaining 1296 chi².
Multiply this by the height of 4 chi 5 cun, obtaining 5832 chi³.
Divide this by 18, obtaining 324 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen, obtaining the result.

Answer: *a*(=200) hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # 4 chi 5 cun = 4 + 5/10 chi

# 列下周三十六尺自相乘得一千二百九十六尺
積 = 下周 * 下周  # 36 * 36 = 1296 chi²

# 以高四尺五寸乘之得五千八百三十二尺
體積 = 積 * 高  # 1296 * 4.5 = 5832 chi³

# 以十八除之得三百二十四尺
體積 = Fraction(體積, 18)  # 5832 / 18 = 324 chi³

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen = 1 + 6/10 + 2/100 chi

# 以斛法除之即得
a = Fraction(體積, 斛法)  # 324 / 1.62 = 200 hu
"""
"""
