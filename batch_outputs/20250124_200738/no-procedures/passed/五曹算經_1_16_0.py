"""
今有圓田周七十八步徑二十六步。問：為田㡬何？
答曰： a畝 奇 b步 。
"""

#----- content starts here -----
"""
Suppose there is a circular field with a circumference of 78 bu and a diameter of 26 bu.
Question: how large is the area of the field?

Answer: it is *a* mu and *b* bu.
"""

# Importing Fraction to handle fractional values
from fractions import Fraction

# 圓田周 (circumference) = 78 步
周 = 78

# 圓田徑 (diameter) = 26 步
徑 = 26

# 圓田面積公式: 面積 = (徑 * 徑 * 3) / 4
面積 = Fraction(徑 * 徑 * 3, 4)

# Convert the area into mu and bu
# 1 畝 = 240 步
a = 面積 // 240  # Integer part (mu)
b = 面積 % 240   # Remainder (bu)

# Output the results
a, b  # a 畝 and b 步#----- content ends here -----

"""
"""
