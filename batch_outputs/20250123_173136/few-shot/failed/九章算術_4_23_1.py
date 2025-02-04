"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""
Suppose there is a volume of 16,448,664,375,000 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says: Place the volume in cubic chi, multiply it by 16.
Divide the result by 9, then extract the cube root.
The result is the diameter of the sphere.

Answer: *a* chi.
"""

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積 = 16448664375000

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# To extract the cube root, we raise the value to the power of 1/3.
a = 積除九 ** Fraction(1, 3)
"""
Variable 'a' has wrong value. Expected: 14300, Actual: 30808.41606745592"""
