"""
今有粟七斗九升。問：為御米幾何？
術曰：置七斗九升以御米率二十一乘之，得一千六百五十九，為實，以粟率五十除之，即得。
答曰： a斗 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9
# 1斗 = 10升, 所以總粟數為：
粟 = 10 * 粟斗 + 粟升

# 御米率二十一
御米率 = 21

# 置七斗九升以御米率二十一乘之，得實
實 = 粟 * 御米率

# 粟率五十
粟率 = 50

# 以粟率五十除之，即得
a = Fraction(實, 粟率)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 1659/50"""
