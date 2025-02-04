"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a square fort with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the volume?

The procedure says: Multiply the side length by itself, then multiply by the height to obtain the volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# 方堡壔方一丈六尺 (convert to chi)
side_length = 1 * 10 + 6  # 1 zhang = 10 chi, so 1 zhang 6 chi = 16 chi

# 高一丈五尺 (convert to chi)
height = 1 * 10 + 5  # 1 zhang 5 chi = 15 chi

# 方自乘 (side length squared)
base_area = side_length * side_length

# 以高乘之，即積尺 (multiply by height to get volume)
volume = base_area * height

# Answer
a = volume
a#----- content ends here -----

"""
"""
