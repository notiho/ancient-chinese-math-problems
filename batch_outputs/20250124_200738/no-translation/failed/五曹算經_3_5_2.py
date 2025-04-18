"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
術曰：列豆八百四十九斛，以七十乘之得五萬九千四百三十斛，以九十除之即得。
答曰： a斛 奇 b升 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 豆八百四十九斛
豆 = 849

# 凡豆九斗易麻七斗
豆換麻比率 = Fraction(7, 9)

# 列豆八百四十九斛，以七十乘之
麻總量 = 豆 * 7

# 以九十除之即得
麻 = Fraction(麻總量, 9)

# 分解為斛與升
a = 麻.numerator // 麻.denominator  # 斛
b = (麻 - a) * 10  # 升
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""
