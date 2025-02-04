"""
今有豆八百四十九斛，凡豆九斗易麻七斗。問：得麻㡬何？
答曰： a斛 奇 b升 。
"""

#----- content starts here -----
"""
Suppose there are 849 hu of beans. For every 9 dou of beans, 7 dou of hemp is exchanged.
Question: how much hemp is obtained?

Answer: *a* hu and *b* sheng.
"""

from fractions import Fraction

# Total beans in hu
豆 = 849

# Conversion rate: 9 dou of beans = 7 dou of hemp
豆換麻率 = Fraction(7, 9)

# Convert beans from hu to dou (1 hu = 10 dou)
豆斗 = 豆 * 10

# Calculate total hemp in dou
麻斗 = 豆斗 * 豆換麻率

# Convert hemp from dou to hu and sheng (1 hu = 10 dou, 1 dou = 10 sheng)
麻斛 = 麻斗 // 10  # Whole hu
麻升 = (麻斗 % 10) * 10  # Remaining sheng

# Final result
a = 麻斛
b = 麻升

a, b  # Output the result as hu and sheng#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 660333/1000, Actual: 660
Variable 'b' has wrong value. Expected: 3, Actual: 100/3"""
