"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
術曰：列下周五十四尺自相乘得二千九百一十六尺以高五尺乘之得一萬四千五百八十尺以九除之得一千六百二十尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 列下周五十四尺
下周 = 54

# 自相乘得二千九百一十六尺
積 = 下周 * 下周

# 以高五尺乘之
高 = 5
體積 = 積 * 高

# 以九除之
體積 = Fraction(體積, 9)

# 以斛法一尺六寸二分除之
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)
a = Fraction(體積, 斛法)

# 答曰：a斛
print(a)
#----- content ends here -----


"""

"""


"""
"""
