"""
今有圓錐下周三丈五尺高五丈一尺問積幾何
術曰下周自乘以高乘之三十六而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a circular cone with a base circumference of 3 zhang and 5 chi, and a height of 5 zhang and 1 chi.
Question: what is the volume?

The procedure says: Multiply the base circumference by itself, then multiply by the height.
Divide the result by 36 to obtain the volume.

Answer: *a* chi³.
"""

# 下周三丈五尺 (convert to chi)
下周 = 3 * 10 + 5  # 1 zhang = 10 chi

# 高五丈一尺 (convert to chi)
高 = 5 * 10 + 1  # 1 zhang = 10 chi

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
a = Fraction(積, 36)  # Volume in chi³#----- content ends here -----

"""
"""
