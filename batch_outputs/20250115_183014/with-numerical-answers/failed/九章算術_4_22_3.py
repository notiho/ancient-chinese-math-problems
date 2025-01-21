"""
今有積四千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a(=20)尺 。
"""

"""
Suppose there is a volume of 4500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says: Take the volume in cubic chi, multiply it by 16, and divide by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a*(=20) chi.
"""

# 積四千五百尺
積 = 4500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# Since we cannot use external libraries, we compute the cube root manually.
# Cube root of a number `x` can be approximated by successive approximation.
def cube_root(x):
    guess = x / 3  # Initial guess
    for _ in range(20):  # Perform 20 iterations for refinement
        guess = (2 * guess + x / (guess * guess)) / 3
    return guess

a = round(cube_root(積除九))  # 20 chi
"""
Timed out"""
