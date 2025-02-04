"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,860,867 cubic chi (尺³).
Question: how many chi (尺) is the side length of the cube?

Answer: the side length is *a* chi.
"""

# 積一百八十六萬八百六十七尺
積 = 1860867

# To find the side length of the cube, take the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess
a = 123  # Initial guess based on approximation (cube root of 1860867 is close to 123)

# Verify the result
if a**3 > 積:
    while a**3 > 積:
        a -= 1
elif a**3 < 積:
    while a**3 < 積:
        a += 1

# Final result
a = a - 1 if a**3 > 積 else a  # Adjust if overshot#----- content ends here -----

"""
"""
