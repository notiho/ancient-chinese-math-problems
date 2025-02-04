"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
術曰：周自相乘，以高乘之，十二而一。
荅曰： a(=2112)尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular embankment with a circumference of 4 zhang and 8 chi, and a height of 1 zhang and 1 chi.
Question: what is the volume?

The procedure says: Multiply the circumference by itself, then multiply by the height, and divide by 12.

Answer: *a*(=2112) chi³.
"""

# 周四丈八尺
周 = 4 * 10 + 8  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈一尺
高 = 1 * 10 + 1  # Convert zhang to chi (1 zhang = 10 chi)

# 周自相乘
周平方 = 周 * 周

# 以高乘之
積 = 周平方 * 高

# 十二而一
a = Fraction(積, 12)  # 2112 chi³#----- content ends here -----

"""
"""
