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

# 1斗 = 10升, convert to total 升
粟總升 = 粟斗 * 10 + 粟升

# 御米率二十一
御米率 = 21

# 置七斗九升以御米率二十一乘之，得實
實 = 粟總升 * 御米率

# 粟率五十
粟率 = 50

# 以粟率五十除之，即得
a = Fraction(實, 粟率) / 10  # Convert back to 斗

print(f"為御米 {a}斗。")
#----- content ends here -----


"""

"""


"""
"""
