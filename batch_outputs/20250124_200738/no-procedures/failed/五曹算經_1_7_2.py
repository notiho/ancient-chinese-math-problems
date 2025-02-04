"""
今有蛇田頭廣三十三步胷廣五十七步尾廣十八步從九十二步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a snake-shaped field. The width at the head is 33 bu, the width at the middle (chest) is 57 bu, and the width at the tail is 18 bu. The length of the field is 92 bu.
Question: How large is the field?

Answer: The field is *a* mu and *b* bu.
"""

from fractions import Fraction

# 頭廣三十三步
頭廣 = 33

# 胸廣五十七步
胸廣 = 57

# 尾廣十八步
尾廣 = 18

# 從九十二步
從 = 92

# Calculate the average width using the formula: (頭廣 + 4 * 胸廣 + 尾廣) / 6
平均廣 = Fraction(頭廣 + 4 * 胸廣 + 尾廣, 6)

# Calculate the total area in bu²: 平均廣 * 從
總面積 = 平均廣 * 從

# Convert the area into mu and remaining bu
# 1 mu = 240 bu²
a = 總面積 // 240  # Integer part (mu)
b = 總面積 % 240   # Remainder (bu)

a, b  # Output the result as (a mu, b bu)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13, Actual: 17
Variable 'b' has wrong value. Expected: 192, Actual: 198"""
