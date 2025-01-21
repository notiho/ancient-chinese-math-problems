"""
今有田形如牛角從五十步口廣二十步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a field shaped like a cow's horn (a trapezoid) with a length of 50 bu and a width at the wider end of 20 bu, while the narrower end is 0 bu.
Question: how large is the area of the field?

Answer: *a* mu and *b* bu.
"""

# Import Fraction for precise calculations
from fractions import Fraction

# 田的形狀為梯形
# 從 (length) = 50 步
從 = 50

# 口廣 (wider end width) = 20 步
口廣 = 20

# 窄端 (narrower end width) = 0 步
窄端 = 0

# 梯形面積公式: 面積 = (上底 + 下底) * 高 / 2
# Here, 上底 = 窄端, 下底 = 口廣, 高 = 從
面積_in_步 = (窄端 + 口廣) * 從 / 2

# 1 畝 = 240 步
# Convert the area into 畝 and 步
a = 面積_in_步 // 240  # Integer part in 畝
b = 面積_in_步 % 240   # Remainder in 步

# Output the results
a = Fraction(a)
b = Fraction(b)

a, b
"""
"""
