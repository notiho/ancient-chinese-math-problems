"""
今有陽馬，廣五尺，袤七尺，高八尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
Suppose there is a wooden horse (陽馬) with a width of 5 chi, a length of 7 chi, and a height of 8 chi.
Question: what is the volume?

The procedure says: Multiply the width and the length, then multiply by the height, and divide by 3.

Answer: *a* chi.
"""

# 廣五尺
廣 = 5

# 袤七尺
袤 = 7

# 高八尺
高 = 8

# 廣袤相乘
廣袤積 = 廣 * 袤

# 以高乘之
體積 = 廣袤積 * 高

# 三而一
a = Fraction(體積, 3)
"""
"""
