"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a wall to be built. The top width is 2 zhang, the bottom width is 5 zhang and 4 chi, the height is 3 zhang and 8 chi, and the length is 5550 chi. Each worker can complete 300 chi³ of work in one autumn.

Question: How many worker-days are required?

Answer: *a* worker-days.
"""

from fractions import Fraction

# Dimensions of the wall
top_width = 2 * 10  # Convert zhang to chi
bottom_width = 5 * 10 + 4  # Convert zhang and chi to chi
height = 3 * 10 + 8  # Convert zhang and chi to chi
length = 5550  # Length in chi

# Worker productivity
worker_productivity = 300  # chi³ per worker in one autumn

# Calculate the average width of the wall
average_width = Fraction(top_width + bottom_width, 2)

# Calculate the volume of the wall
volume = average_width * height * length

# Calculate the number of worker-days required
a = Fraction(volume, worker_productivity)

# Output the result
a#----- content ends here -----

"""
"""
