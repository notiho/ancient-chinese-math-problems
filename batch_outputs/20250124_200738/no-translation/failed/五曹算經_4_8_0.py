"""
今有平地聚粟下周三丈高四尺。問：粟㡬何？
術曰：列下周三十尺自相乘得九百尺以高四尺乘之得三千六百尺以三十六除之得一百尺以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 下周三丈
下周 = 3 * 10  # 1丈 = 10尺

# 高四尺
高 = 4

# 列下周三十尺自相乘得九百尺
積 = 下周 * 下周

# 以高四尺乘之得三千六百尺
積 *= 高

# 以三十六除之得一百尺
積 /= 36

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # 1尺6寸2分

# 以斛法除之即得
粟 = Fraction(積, 斛法)

# 分解為斛和分
a = int(粟)  # 斛
b = (粟 - a) * 100  # 分
#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
