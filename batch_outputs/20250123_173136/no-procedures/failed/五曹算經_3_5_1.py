"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
答曰： a斛 奇 b升 。
"""

"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp can be exchanged.
Question: how much hemp can be obtained?

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# Total beans in hu
total_beans = 849

# Conversion rate: 9 dou of beans = 7 dou of hemp
beans_per_exchange = 9
hemp_per_exchange = 7

# Convert total beans from hu to dou (1 hu = 10 dou)
total_beans_in_dou = total_beans * 10

# Total hemp in dou
total_hemp_in_dou = Fraction(total_beans_in_dou * hemp_per_exchange, beans_per_exchange)

# Convert hemp from dou to hu and sheng (1 hu = 10 dou, 1 dou = 10 sheng)
a = total_hemp_in_dou // 10  # Whole hu
remaining_dou = total_hemp_in_dou % 10
b = remaining_dou * 10  # Convert remaining dou to sheng

a, b  # Final result: a hu and b sheng
"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 100/3"""
