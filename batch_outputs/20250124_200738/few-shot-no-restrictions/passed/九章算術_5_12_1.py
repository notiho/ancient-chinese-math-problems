"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square fort with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the total volume?

The procedure says: Multiply the side length by itself, then multiply by the height. The result is the volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 方堡壔方一丈六尺 (side length: 1 zhang 6 chi)
side_length = 1 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 高一丈五尺 (height: 1 zhang 5 chi)
height = 1 * 10 + 5  # Convert zhang to chi

# 方自乘 (square the side length)
base_area = side_length * side_length

# 以高乘之，即積尺 (multiply by the height to get the volume)
volume = base_area * height

# Answer
a = volume
a#----- content ends here -----

"""
"""
