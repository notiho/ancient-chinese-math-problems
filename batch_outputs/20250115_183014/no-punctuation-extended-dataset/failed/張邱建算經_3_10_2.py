"""
今有窖上廣五尺上袤八尺下廣七尺深九尺受粟三百一斛八㪷八十一分㪷之四十二問下袤幾何
術曰置粟積尺以六乘之深而一所得倍上袤以上廣乘之又以下廣乘上袤併以減之餘以倍下廣上廣從之而一得下袤
答曰 a丈
"""

"""
Suppose there is a granary with the following dimensions:
- Upper width: 5 chi
- Upper length: 8 chi
- Lower width: 7 chi
- Depth: 9 chi
It holds 301斛8斗81/42斗 of millet.
Question: what is the lower length?

The procedure says:
1. Place the millet volume in chi and multiply it by 6. Divide by the depth, obtaining a doubled value.
2. Multiply the upper length by the upper width, then also multiply it by the lower width. Add these together.
3. Subtract the result from the doubled value obtained earlier.
4. Divide the remainder by the sum of the doubled lower width and the upper width. Divide by 1 to obtain the lower length.

Answer: *a* zhang.
"""

from fractions import Fraction

# 上廣五尺
上廣 = 5

# 上袤八尺
上袤 = 8

# 下廣七尺
下廣 = 7

# 深九尺
深 = 9

# 粟三百一斛八斗八十一分斗之四十二
粟 = 301 * 10 + 8 + Fraction(81, 42)  # Convert to dou
粟積尺 = 粟 * 10  # Convert dou to chi^3

# 置粟積尺以六乘之
倍值 = 粟積尺 * 6

# 深而一
倍值 = 倍值 / 深

# 所得倍上袤以上廣乘之
上積 = 倍值 - (上袤 * 上廣 + 上廣 * 下廣)

# 餘以倍下廣上廣從之而一
下袤 = 上積 / (2 * 下廣 + 上廣)

# Convert to zhang (1 zhang = 10 chi)
a = 下袤 / 10
"""
Variable 'a' has wrong value. Expected: 1, Actual: 28081/266"""
