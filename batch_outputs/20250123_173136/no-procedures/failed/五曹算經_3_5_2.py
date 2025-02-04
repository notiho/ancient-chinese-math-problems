"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
答曰： a斛 奇 b升 。
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, you can exchange for 7 dou of hemp.
Question: how much hemp can you obtain?

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# Total beans in hu
total_beans = 849

# Conversion rate: 9 dou of beans = 7 dou of hemp
beans_to_hemp_ratio = Fraction(7, 9)

# Convert total beans (in hu) to dou (1 hu = 10 dou)
total_beans_in_dou = total_beans * 10

# Calculate total hemp in dou
total_hemp_in_dou = total_beans_in_dou * beans_to_hemp_ratio

# Convert total hemp back to hu and sheng
a = total_hemp_in_dou // 10  # Whole hu
b = total_hemp_in_dou % 10  # Remaining dou (1 dou = 10 sheng)

# Convert remaining dou to sheng
b = b * 10  # Remaining sheng

# Final result
a = int(a)  # Whole hu
b = int(b)  # Remaining sheng

a, b  # Output: a hu and b sheng
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 33"""
