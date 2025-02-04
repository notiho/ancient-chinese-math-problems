"""
今有長安、洛陽相去九百里，車輪一匝一丈八尺。欲自洛陽至長安。問：輪匝幾何？
答曰： a 匝。
"""

#----- content starts here -----
"""
Suppose the distance between Chang'an and Luoyang is 900 li. A single rotation of a cartwheel covers 1 zhang and 8 chi (1 zhang = 10 chi).  
Question: how many rotations does the wheel make to travel from Luoyang to Chang'an?

Answer: *a* rotations.
"""

# 長安、洛陽相去九百里
distance_in_li = 900

# Convert li to chi (1 li = 300 chi)
distance_in_chi = distance_in_li * 300

# 車輪一匝一丈八尺 (1 zhang = 10 chi, so 1 zhang 8 chi = 18 chi)
wheel_circumference = 10 + 8  # 18 chi

# Calculate the number of rotations
a = Fraction(distance_in_chi, wheel_circumference)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 90000, Actual: 15000"""
