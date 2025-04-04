"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 去閫一尺
去閫 = 1  # 尺

# 不合二寸
不合 = Fraction(2, 10)  # 2寸 = 2/10尺

# 以去閫一尺自乘，所得
去閫平方 = 去閫 * 去閫

# 以不合二寸半之而一，所得
半之而一 = 去閫平方 / 不合

# 增不合之半
門廣 = 半之而一 + (不合 / 2)

# a為門廣
a = 門廣
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 51/10"""
