"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
術曰：并三廣，以深乘之，又以袤乘之，六而一。
荅曰： a(=84)尺 。
"""

#----- content starts here -----
"""
Suppose there is a truncated prism. Its bottom width is 6 chi, its top width is 10 chi, its depth is 3 chi, and its end width is 8 chi with no depth, and its length is 7 chi.
Question: what is its volume?

The procedure says: Add the three widths together, multiply by the depth, then multiply by the length, and divide by 6.

Answer: *a*(=84) chi³.
"""

# 下廣六尺
下廣 = 6

# 上廣一丈 (1丈 = 10尺)
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
a = Fraction(總積, 6) # 84
#----- content ends here -----

"""
"""
