"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
術曰：下周自乘，以高乘之，三十六而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular cone with a base circumference of 3 zhang and 5 chi, and a height of 5 zhang and 1 chi.
Question: what is the volume?

The procedure says: Multiply the base circumference by itself, then multiply by the height, and divide by 36.

Answer: *a* chi³.
"""

# 下周三丈五尺
下周 = 3 * 10 + 5  # Convert zhang to chi (1 zhang = 10 chi)

# 高五丈一尺
高 = 5 * 10 + 1  # Convert zhang to chi

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
a = Fraction(積, 36)  # Volume in chi³#----- content ends here -----

"""
"""
