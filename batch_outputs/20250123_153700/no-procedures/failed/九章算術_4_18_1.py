"""
今有積一百八十六萬八百六十七尺。問︰為立方幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,860,867 cubic chi (尺³).
Question: how many chi (尺) is the side length of the cube?

Answer: the side length is *a* chi.
"""

# 積一百八十六萬八百六十七尺
積 = 1860867

# To find the side length of the cube, we calculate the cube root of the volume.
# Since we cannot use external libraries, we use an iterative method to approximate the cube root.

def cube_root(n):
    # Start with an initial guess
    guess = Fraction(1)
    while True:
        # Newton's method for cube root: x = (2x + n / x^2) / 3
        next_guess = (2 * guess + n / (guess * guess)) / 3
        if next_guess == guess:  # Convergence check
            break
        guess = next_guess
    return guess

# Calculate the cube root of the volume
a = cube_root(Fraction(積))

# The side length of the cube is `a` chi.
"""
Timed out"""
