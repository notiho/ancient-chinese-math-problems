"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a square fortress with a side length of 1 zhang and 6 chi, and a height of 1 zhang and 5 chi.
Question: what is the total volume?

Answer: the volume is *a* cubic chi.
"""

# Side length of the square base (1 zhang = 10 chi, so 1 zhang 6 chi = 10 + 6 = 16 chi)
side_length = 10 + 6

# Height of the fortress (1 zhang 5 chi = 10 + 5 = 15 chi)
height = 10 + 5

# Volume of the fortress = side_length^2 * height
a = Fraction(side_length**2 * height)

# Result
a
"""
"""
