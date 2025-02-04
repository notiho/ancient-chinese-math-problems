"""
今有窖上廣五尺上袤八尺下廣七尺深九尺受粟三百一斛八㪷八十一分㪷之四十二問下袤幾何
術曰置粟積尺以六乘之深而一所得倍上袤以上廣乘之又以下廣乘上袤併以減之餘以倍下廣上廣從之而一得下袤
答曰 a丈
"""

"""
Suppose there is a granary with the following dimensions:
- Top width: 5 chi
- Top length: 8 chi
- Bottom width: 7 chi
- Depth: 9 chi
It holds 301斛8斗81/42斗 of millet.
Question: what is the bottom length?

The procedure says:
1. Place the millet volume in chi, multiply it by 6, and divide by the depth.
2. Double the result, then multiply it by the top length and the top width.
3. Also multiply it by the bottom width.
4. Add the product of the top length and the top width, then subtract it from the previous result.
5. Take the remainder, divide it by twice the bottom width plus the top width, and divide again by 1.
6. The result is the bottom length.

Answer: *a* zhang.
"""

from fractions import Fraction

# Granary dimensions
上廣 = 5  # Top width in chi
上袤 = 8  # Top length in chi
下廣 = 7  # Bottom width in chi
深 = 9    # Depth in chi

# Volume of millet in chi
粟積 = 300 * 10 + 8 + Fraction(81, 42)  # Convert 301斛8斗81/42斗 to chi

# Step 1: Multiply millet volume by 6 and divide by depth
step1 = Fraction(粟積 * 6, 深)

# Step 2: Double the result, then multiply by top length and top width
step2 = 2 * step1 * 上袤 * 上廣

# Step 3: Also multiply by bottom width
step3 = step1 * 下廣

# Step 4: Add the product of top length and top width, then subtract it from the previous result
step4 = step2 + step3 - (上袤 * 上廣)

# Step 5: Divide the remainder by twice the bottom width plus the top width
step5 = Fraction(step4, 2 * 下廣 + 上廣)

# Step 6: Divide again by 1 (no change here)
a = step5 / 1  # Bottom length in zhang

a
"""
Variable 'a' has wrong value. Expected: 1, Actual: 1221751/133"""
