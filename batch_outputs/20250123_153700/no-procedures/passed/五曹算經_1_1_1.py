"""
今有方田廣從各六十八步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a square field with both width and length of 68 bu.
Question: how large is the field?

Answer: it is *a* mu and *b* bu.
"""

from fractions import Fraction

# 方田廣從各六十八步
邊長 = 68

# 計算田的面積 (平方面積)
面積_步 = 邊長 * 邊長

# 1 畝 = 240 步
# 計算畝數
a = 面積_步 // 240

# 計算剩餘的步數
b = 面積_步 % 240

# Output the result
a, b
"""
"""
