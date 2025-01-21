"""
今有羨除下廣六尺上廣一丈深三尺末廣八尺無深袤七尺問積幾何
術曰并三廣以深乘之又以袤乘之六而一
荅曰 a尺 
"""

"""
Suppose there is a truncated prism with a bottom width of 6 chi, a top width of 10 chi, a depth of 3 chi, and an intermediate width of 8 chi without depth. Its length is 7 chi.
Question: what is the volume?

The procedure says: Add the three widths together, multiply by the depth, and then multiply by the length. Divide by 6.

Answer: *a* chi.
"""

# 下廣六尺
下廣 = 6

# 上廣一丈 (10 尺)
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
