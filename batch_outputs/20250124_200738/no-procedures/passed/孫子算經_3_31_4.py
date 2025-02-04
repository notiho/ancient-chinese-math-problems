"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
答曰： a 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A single rotation of the cartwheel covers 1 zhang and 8 chi (1 zhang = 10 chi).
Question: how many rotations does the wheel make to travel from Luoyang to Chang'an?

Answer: *a* rotations.
"""

# 長安、洛陽相去九百里
distance_in_li = 900

# 1 里 = 180 丈
distance_in_zhang = distance_in_li * 180

# 車輪一匝一丈八尺 (1 丈 = 10 尺, so 1 丈 8 尺 = 18 尺)
wheel_circumference_in_zhang = Fraction(18, 10)

# Calculate the number of rotations
a = Fraction(distance_in_zhang, wheel_circumference_in_zhang)

# Output the result
a#----- content ends here -----

"""
"""
