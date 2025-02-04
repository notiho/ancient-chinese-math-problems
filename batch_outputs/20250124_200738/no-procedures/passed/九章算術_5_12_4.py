"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square fortress with a side length of 1 zhang 6 chi and a height of 1 zhang 5 chi.
Question: what is the volume of the fortress?

Answer: *a* cubic chi.
"""

# 方堡壔方一丈六尺 (side length of the square base)
side_length = 1 * 10 + 6  # Convert 1 zhang 6 chi to chi

# 高一丈五尺 (height of the fortress)
height = 1 * 10 + 5  # Convert 1 zhang 5 chi to chi

# Volume of the fortress
a = side_length * side_length * height  # Volume = side^2 * height

a  # The result is in cubic chi#----- content ends here -----

"""
"""
