"""
今有內角聚粟下周五十四尺高五尺。問：粟㡬何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a granary in the shape of a cone, with a base circumference of 54 chi and a height of 5 chi.
Question: how much millet can it hold?

Answer: it holds *a* hu.
"""

# 周五十四尺 (circumference of the base)
周 = 54

# 高五尺 (height of the cone)
高 = 5

# The formula for the volume of a cone is: V = (1/3) * base_area * height
# The base area of a circle is: base_area = (circumference^2) / (4 * π)
# For simplicity, use π ≈ 3

π = 3

# Calculate the base area
底面積 = Fraction(周**2, 4 * π)

# Calculate the volume of the cone
體積 = Fraction(1, 3) * 底面積 * 高

# Convert the volume from cubic chi to hu (1 hu = 10 cubic chi)
a = Fraction(體積, 10)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1000, Actual: 81/2"""
