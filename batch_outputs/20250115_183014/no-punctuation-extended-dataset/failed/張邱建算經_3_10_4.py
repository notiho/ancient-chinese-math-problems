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
5. Take the remainder, divide it by twice the bottom width plus the top width, and divide by 1 to obtain the bottom length.

Answer: the bottom length is *a* zhang.
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
粟積尺 = 粟 * 10  # Convert to chi^3 (1 dou = 10 chi^3)

# 置粟積尺以六乘之
積六乘 = 粟積尺 * 6

# 深而一
積深除 = 積六乘 / 深

# 所得倍
倍積 = 2 * 積深除

# 上袤以上廣乘之
上袤廣積 = 上袤 * 上廣

# 又以下廣乘
下廣積 = 倍積 * 下廣

# 上袤併
上袤併積 = 倍積 * 上袤廣積

# 以減之
餘 = 下廣積 - 上袤併積

# 餘以倍下廣上廣從之而一
法 = 2 * 下廣 + 上廣
a = Fraction(餘, 法) / 10  # Convert to zhang (1 zhang = 10 chi)
"""
Variable 'a' has wrong value. Expected: 1, Actual: -930138/133"""
