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
豆率 = 9  # 豆九斗
麻率 = 7  # 麻七斗

# 列豆八百四十九斛，以七十乘之
麻總量 = 豆 * 麻率

# 以九十除之即得
a = 麻總量 // 豆率  # 得到整斛數
b = Fraction(麻總量 % 豆率, 豆率) * 10  # 剩餘部分轉為升

# 答案
a斛 = a
b升 = b
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 10/3"""
