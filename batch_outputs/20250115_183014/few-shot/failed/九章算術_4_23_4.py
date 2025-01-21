"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,648,466,437,500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says: Place the volume in cubic chi.
Multiply it by 16.
Divide it by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a* chi.
"""

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積 = 1648466437500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# To compute the cube root, we use exponentiation with 1/3.
a = 積除九 ** Fraction(1, 3)
"""
Variable 'a' has wrong value. Expected: 14300, Actual: 14310.424856303918"""
