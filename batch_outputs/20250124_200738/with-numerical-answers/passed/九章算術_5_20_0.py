"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a(=70/3)尺 。
"""

#----- content starts here -----
"""
Suppose there is a truncated pyramid (a frustum) with a lower base width of 5 chi and no length, an upper base length of 4 chi and no width, and a height of 7 chi.
Question: what is its volume?

The procedure says: Multiply the width and length together, then multiply by the height, and divide by 6.

Answer: *a*(=70/3) chi³.
"""

# 下廣五尺
下廣 = 5

# 上袤四尺
上袤 = 4

# 高七尺
高 = 7

# 廣袤相乘
廣袤積 = 下廣 * 上袤

# 以高乘之
體積積 = 廣袤積 * 高

# 六而一
a = Fraction(體積積, 6) # 70/3 chi³#----- content ends here -----

"""
"""
