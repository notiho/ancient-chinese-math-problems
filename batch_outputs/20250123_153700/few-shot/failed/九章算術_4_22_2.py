"""
今有積四千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""
Suppose there is a volume of 4500 cubic chi.
Question: what is the diameter of the inscribed sphere?

The procedure for finding the diameter of the inscribed sphere says: Place the volume in cubic chi.
Multiply it by 16.
Divide it by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a* chi.
"""

# 積四千五百尺
積 = 4500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# To compute the cube root manually, we use an iterative approximation method.
def cube_root(n, precision=10):
    guess = n / 3  # Initial guess
    for _ in range(precision):
        guess = (2 * guess + n / (guess * guess)) / 3
    return guess

a = cube_root(積除九)  # 丸徑
"""
Variable 'a' has wrong value. Expected: 20, Actual: Too large to be printed"""
