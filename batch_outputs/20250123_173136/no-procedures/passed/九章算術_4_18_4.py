"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,860,867 cubic chi (尺).
Question: how many chi (尺) is the side length of the cube?

Answer: the side length is *a* chi.
"""

# 積一百八十六萬八百六十七尺
積 = 1860867

# To find the side length of the cube, take the cube root of the volume.
# Since we cannot use external libraries, we will approximate the cube root manually.

# Start with an initial guess for the cube root
a = 120  # Initial guess (close to the actual cube root of 1860867)

# Refine the guess using a simple iterative method
for _ in range(10):  # Perform 10 iterations for better accuracy
    a = Fraction(2 * a + 積 // (a * a), 3)

# The final value of `a` is the side length of the cube in chi.
a
"""
"""
