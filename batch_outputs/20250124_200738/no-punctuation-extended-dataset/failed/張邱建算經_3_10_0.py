"""
今有窖上廣五尺上袤八尺下廣七尺深九尺受粟三百一斛八㪷八十一分㪷之四十二問下袤幾何
術曰置粟積尺以六乘之深而一所得倍上袤以上廣乘之又以下廣乘上袤併以減之餘以倍下廣上廣從之而一得下袤
答曰 a丈
"""

#----- content starts here -----
"""
Suppose there is a granary with the following dimensions:
- Top width: 5 chi
- Top length: 8 chi
- Bottom width: 7 chi
- Depth: 9 chi
It holds 301斛8斗81/42斗 of millet.
Question: What is the bottom length?

The procedure says:
1. Place the millet volume in chi and multiply it by 6.
2. Divide by the depth, obtaining a value.
3. Double the top length and multiply it by the top width.
4. Also multiply it by the bottom width.
5. Add the top length to the bottom width, then subtract the previous result.
6. Take the remainder and divide it by twice the bottom width plus the top width.
7. Divide by 1 to obtain the bottom length.

Answer: The bottom length is *a* zhang.
"""

from fractions import Fraction

# Dimensions of the granary
上廣 = 5  # Top width in chi
上袤 = 8  # Top length in chi
下廣 = 7  # Bottom width in chi
深 = 9    # Depth in chi

# Volume of millet in chi (convert from 301斛8斗81/42斗 to chi)
粟積 = 301 * 10 + 8 + Fraction(81, 42)

# Step 1: Multiply millet volume by 6
粟積乘六 = 6 * 粟積

# Step 2: Divide by the depth
值 = 粟積乘六 / 深

# Step 3: Double the top length and multiply by the top width
倍上袤 = 2 * 上袤
倍上袤乘上廣 = 倍上袤 * 上廣

# Step 4: Multiply by the bottom width
倍上袤乘上廣乘下廣 = 倍上袤乘上廣 * 下廣

# Step 5: Add the top length to the bottom width, then subtract the previous result
上袤加下廣 = 上袤 + 下廣
餘 = 值 - 倍上袤乘上廣乘下廣

# Step 6: Divide by twice the bottom width plus the top width
分母 = 2 * 下廣 + 上廣
下袤 = 餘 / 分母

# Step 7: Divide by 1 to obtain the bottom length
a = 下袤 / 1  # Result in zhang (1 zhang = 10 chi)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 10173/133"""
