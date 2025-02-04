"""
今有圓錐下周三丈五尺，高五丈一尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a cone with a base circumference of 3 zhang 5 chi and a height of 5 zhang 1 chi.
Question: what is the volume of the cone?

Answer: the volume is *a* cubic chi.
"""

# 下周三丈五尺 (convert to chi)
下周 = 3 * 10 + 5  # 1 zhang = 10 chi

# 高五丈一尺 (convert to chi)
高 = 5 * 10 + 1  # 1 zhang = 10 chi

# 圓錐公式: 體積 = (1/3) * 底面積 * 高
# 底面積公式: 面積 = (周長^2) / (4 * π)
# Approximate π as 3 for simplicity (as was often done in ancient Chinese mathematics)

π = 3

# Calculate the radius from the circumference
半徑 = 下周 / (2 * π)

# Calculate the base area
底面積 = (半徑 ** 2) * π

# Calculate the volume of the cone
a = Fraction(1, 3) * 底面積 * 高

# Simplify the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 20825/12, Actual: 1735.4166666666663"""
