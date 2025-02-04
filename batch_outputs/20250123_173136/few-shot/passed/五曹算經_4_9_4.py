"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
術曰：列下周五十四尺自相乘得二千九百一十六尺以高五尺乘之得一萬四千五百八十尺以九除之得一千六百二十尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

"""
Suppose there is a granary with a circular base, where the circumference of the base is 54 chi, and the height is 5 chi.
Question: how much millet can it hold?

The procedure says: Take the circumference of the base (54 chi), square it to get 2916 chi². 
Multiply this by the height (5 chi) to get 14580 chi³.
Divide this by 9 to get 1620 chi³.
Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen = 1.62 chi³) to obtain the number of hu.

Answer: it holds *a* hu.
"""

from fractions import Fraction

# 下周五十四尺
下周 = 54

# 高五尺
高 = 5

# 列下周五十四尺自相乘得二千九百一十六尺
基面積 = 下周 * 下周

# 以高五尺乘之得一萬四千五百八十尺
體積 = 基面積 * 高

# 以九除之得一千六百二十尺
體積除九 = Fraction(體積, 9)

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)

# 以斛法除之即得
a = Fraction(體積除九, 斛法)
"""
"""
