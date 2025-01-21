"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
答曰： a斛 奇 b升 。
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, you can exchange for 7 dou of hemp.
Question: how much hemp can you get?

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# Total beans in hu
total_beans = 849

# Conversion rate: 9 dou of beans = 7 dou of hemp
beans_to_hemp_ratio = Fraction(7, 9)

# Convert beans to hemp in hu
total_hemp_in_hu = total_beans * beans_to_hemp_ratio

# Separate into hu and sheng
a = int(total_hemp_in_hu)  # Whole hu
remaining_hemp = total_hemp_in_hu - a  # Remaining fraction of hu
b = int(remaining_hemp * 10)  # Convert remaining hu to sheng (1 hu = 10 dou)

a, b
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660"""
