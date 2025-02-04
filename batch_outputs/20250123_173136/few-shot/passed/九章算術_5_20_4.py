"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，六而一。
荅曰： a尺 。
"""

"""
Suppose there is a turtle-shell-shaped solid with a lower width of 5 chi (no length), an upper length of 4 chi (no width), and a height of 7 chi.
Question: what is the volume?

The procedure says: Multiply the width and length, then multiply by the height, and divide by 6.

Answer: *a* cubic chi.
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
體積 = 廣袤積 * 高

# 六而一
a = Fraction(體積, 6)
"""
"""
