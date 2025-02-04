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
# Since we cannot use external libraries, we calculate the square root manually
a = 0
while a * a < 積:
    a += 1

# Check if the square is exact
if a * a != 積:
    a -= 1  # Adjust if overshot

# Final result
a#----- content ends here -----

"""
"""
