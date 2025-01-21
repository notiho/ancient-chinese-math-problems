"""
今有粟七斗九升。問：為御米幾何？
術曰：置七斗九升以御米率二十一乘之，得一千六百五十九，為實，以粟率五十除之，即得。
答曰： a斗 。
"""

"""

"""


from fractions import Fraction

# 粟七斗九升
粟斗 = 7
粟升 = 9

# Convert 粟 to 升 (1斗 = 10升)
粟 = 粟斗 * 10 + 粟升

# 御米率二十一
御米率 = 21

# 置七斗九升以御米率二十一乘之，得實
實 = 粟 * 御米率

# 粟率五十
粟率 = 50

# 以粟率五十除之，即得
a = Fraction(實, 粟率)

# Convert result back to 斗 and 升
斗 = a // 10  # Whole number of 斗
升 = a % 10   # Remaining 升

print(f"答曰：{斗}斗 {升}升")


"""

"""


"""
Variable 'a' has wrong value. Expected: 1659/500, Actual: 1659/50"""
