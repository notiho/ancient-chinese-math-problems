"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
術曰：列下周五十四尺自相乘得二千九百一十六尺以高五尺乘之得一萬四千五百八十尺以九除之得一千六百二十尺以斛法一尺六寸二分除之即得。
答曰： a(=1000)斛 。
"""

"""
Suppose there is a granary with an inner base circumference of 54 chi and a height of 5 chi.
Question: how much millet does it hold?

The procedure says: Take the base circumference of 54 chi, multiply it by itself, obtaining 2916 chi².
Multiply this by the height of 5 chi, obtaining 14580 chi³.
Divide this by 9, obtaining 1620 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen (1.62 chi), obtaining the result.

Answer: *a*(=1000) hu.
"""

from fractions import Fraction

# 下周五十四尺
下周 = 54

# 高五尺
高 = 5

# 斛法一尺六寸二分
斛法 = Fraction(162, 100)  # 1 chi 6 cun 2 fen = 1.62 chi

# 列下周五十四尺自相乘得二千九百一十六尺
積 = 下周 * 下周

# 以高五尺乘之得一萬四千五百八十尺
體積 = 積 * 高

# 以九除之得一千六百二十尺
體積 = Fraction(體積, 9)

# 以斛法一尺六寸二分除之即得
a = Fraction(體積, 斛法)  # 1000 hu
"""
"""
