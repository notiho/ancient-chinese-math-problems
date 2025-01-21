"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

"""
Suppose there is a snake-shaped field. The width at the head is 33 bu, the width at the middle is 57 bu, the width at the tail is 18 bu, and the length is 92 bu.
Question: how large is the field?

Answer: *a* mu and *b* bu.
"""

from fractions import Fraction

# 頭廣 (width at the head)
頭廣 = 33

# 胸廣 (width at the middle)
胸廣 = 57

# 尾廣 (width at the tail)
尾廣 = 18

# 從 (length)
從 = 92

# Calculate the average width
平均廣 = Fraction(頭廣 + 4 * 胸廣 + 尾廣, 6)

# Calculate the total area in bu²
總面積 = 平均廣 * 從

# Convert to mu and bu
a = 總面積 // 240  # 1 mu = 240 bu²
b = 總面積 % 240  # Remaining bu²

a, b  # Output the result as (a mu, b bu)
"""
Variable 'a' has wrong value. Expected: 13, Actual: 17
Variable 'b' has wrong value. Expected: 192, Actual: 198"""
