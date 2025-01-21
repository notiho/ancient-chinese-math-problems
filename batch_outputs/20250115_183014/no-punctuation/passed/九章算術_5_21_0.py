"""
今有羨除下廣六尺上廣一丈深三尺末廣八尺無深袤七尺問積幾何
術曰并三廣以深乘之又以袤乘之六而一
荅曰 a尺 
"""

"""
Suppose there is a truncated prism (a frustum) with the following dimensions:
The bottom width is 6 chi, the top width is 10 chi, the depth is 3 chi, and the middle width is 8 chi.
The length (mao) is 7 chi.
Question: what is the volume?

The procedure says: Add the three widths together, multiply by the depth, and then multiply by the length.
Finally, divide by 6.

The answer says: *a* chi³.
"""

# 下廣六尺
下廣 = 6

# 上廣一丈 (convert to chi: 1丈 = 10尺)
上廣 = 10

# 末廣八尺
末廣 = 8

# 深三尺
深 = 3

# 袤七尺
袤 = 7

# 并三廣
三廣和 = 下廣 + 上廣 + 末廣

# 以深乘之
深積 = 三廣和 * 深

# 又以袤乘之
總積 = 深積 * 袤

# 六而一
a = Fraction(總積, 6)
"""
"""
