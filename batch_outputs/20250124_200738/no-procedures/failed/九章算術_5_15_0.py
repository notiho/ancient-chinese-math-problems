"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a circular pavilion with the bottom circumference of 3 zhang, the top circumference of 2 zhang, and a height of 1 zhang.
Question: what is the volume?

Answer: *a* chi³.
"""

# 下周三丈 (bottom circumference)
下周 = 3 * 10  # Convert zhang to chi

# 上周二丈 (top circumference)
上周 = 2 * 10  # Convert zhang to chi

# 高一丈 (height)
高 = 1 * 10  # Convert zhang to chi

# Calculate the average circumference
平均周 = Fraction(下周 + 上周, 2)

# Calculate the radius using the formula: circumference = 2 * pi * radius
# Here, we approximate pi as 3 (as was common in ancient Chinese mathematics)
平均徑 = Fraction(平均周, 3)

# Calculate the area of the circular cross-section: area = pi * r^2
平均面積 = 3 * (平均徑 / 2) ** 2

# Calculate the volume: volume = average area * height
a = 平均面積 * 高  # Volume in chi³

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 3125/6"""
