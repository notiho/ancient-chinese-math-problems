"""
今有鱉臑下廣五尺，無袤，上袤四尺，無廣，高七尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a truncated pyramid-like object (a frustum) with the following dimensions:
- The bottom width is 5 chi.
- The bottom length is unknown (assume it is square, so the length equals the width).
- The top length is 4 chi.
- The top width is unknown (assume it is square, so the width equals the length).
- The height is 7 chi.

Question: What is the volume of the object?

Answer: The volume is *a* cubic chi.
"""

# Bottom width and length (square base)
bottom_width = 5
bottom_length = 5

# Top width and length (square top)
top_width = 4
top_length = 4

# Height
height = 7

# Formula for the volume of a frustum of a square pyramid:
# V = (1/3) * height * (A1 + A2 + sqrt(A1 * A2))
# where A1 = area of the bottom square, A2 = area of the top square

# Calculate areas of the bottom and top squares
A1 = bottom_width * bottom_length
A2 = top_width * top_length

# Calculate the volume
a = Fraction(1, 3) * height * (A1 + A2 + (A1 * A2) ** 0.5)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 70/3, Actual: 142.33333333333334"""
