"""
今有積五萬五千二百二十五步。問︰為方幾何？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a total area of 55,225 square bu.
Question: what is the side length of the square field?

Answer: the side length is *a* bu.
"""

# 積五萬五千二百二十五步
積 = 55225

# To find the side length of a square, take the square root of the area
# The square root of a perfect square can be found by repeated subtraction of odd numbers
side_length = 0
current_sum = 0
odd_number = 1

while current_sum < 積:
    current_sum += odd_number
    odd_number += 2
    side_length += 1

# The side length of the square
a = side_length#----- content ends here -----

"""
"""
