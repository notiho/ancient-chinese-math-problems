"""
今有圓堡壔周四丈八尺高一丈一尺問積幾何
術曰周自相乘以高乘之十二而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a circular fort with a circumference of 4 zhang and 8 chi, and a height of 1 zhang and 1 chi.
Question: what is the volume?

The procedure says: Multiply the circumference by itself, then multiply by the height. Divide by 12 to get the volume.

Answer: *a* chi³.
"""

# 周四丈八尺
周 = 4 * 10 + 8  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈一尺
高 = 1 * 10 + 1  # Convert zhang to chi

# 周自相乘
周平方 = 周 * 周

# 以高乘之
積 = 周平方 * 高

# 十二而一
a = Fraction(積, 12)  # Volume in chi³#----- content ends here -----

"""
"""
