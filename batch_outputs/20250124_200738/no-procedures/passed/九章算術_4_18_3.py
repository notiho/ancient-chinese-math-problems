"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a total volume of 1,860,867 cubic chi.
Question: how many chi does the cube's side measure?

Answer: the side length is *a* chi.
"""

# Given total volume
積 = 1860867

# To find the side length of the cube, we calculate the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess
a = 123  # Initial guess based on estimation

# Refine the guess using a simple iterative method
while a**3 < 積:
    a += 1

# If the cube of the current guess exceeds the volume, subtract 1 to get the correct value
if a**3 > 積:
    a -= 1

# The final value of `a` is the side length of the cube in chi.
a#----- content ends here -----

"""
"""
