"""
今有陽馬，廣五尺，袤七尺，高八尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，三而一。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a wooden horse (陽馬) with a width of 5 chi, a length of 7 chi, and a height of 8 chi.
Question: what is the volume?

The procedure says: Multiply the width and the length, then multiply the result by the height, and divide by 3.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Dimensions of the wooden horse
廣 = 5  # Width in chi
袤 = 7  # Length in chi
高 = 8  # Height in chi

# Calculate the volume
積 = (廣 * 袤 * 高) / 3

# Represent the result as a fraction
a = Fraction(積)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 280/3, Actual: 6567749456581973/70368744177664"""
