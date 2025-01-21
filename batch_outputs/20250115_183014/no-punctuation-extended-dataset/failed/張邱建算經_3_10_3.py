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
5. Take the remainder and divide it by the sum of twice the bottom width and the top width.
6. Divide by 1 to obtain the bottom length.

Answer: *a* zhang.
"""

from fractions import Fraction

# Given dimensions and volume
上廣 = 5  # chi
上袤 = 8  # chi
下廣 = 7  # chi
深 = 9  # chi
粟積 = 300 * 10 + 8 + Fraction(81, 42)  # Convert 301斛8斗81/42斗 to chi³

# Step 1: Place the millet volume in chi, multiply it by 6, and divide by the depth
積尺 = Fraction(粟積 * 6, 深)

# Step 2: Double the result, then multiply it by the top length and the top width
倍積 = 2 * 積尺
上積 = 倍積 * 上袤 * 上廣

# Step 3: Also multiply it by the bottom width
下積 = 倍積 * 下廣

# Step 4: Add the product of the top length and the top width, then subtract it from the previous result
減積 = 上積 + (上袤 * 上廣)
餘積 = 下積 - 減積

# Step 5: Take the remainder and divide it by the sum of twice the bottom width and the top width
分母 = 2 * 下廣 + 上廣
下袤 = Fraction(餘積, 分母)

# Step 6: Divide by 1 to obtain the bottom length
a = 下袤 / 1  # Convert to zhang (if needed, divide by 10 for zhang)

a  # Answer in chi
"""
Variable 'a' has wrong value. Expected: 1, Actual: -927338/133"""
