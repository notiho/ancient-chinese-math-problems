"""
今有積四千五百尺問為立圓徑幾何
開立圓術曰置積尺數以十六乘之九而一所得開立方除之即丸徑
荅曰 a尺 
"""

"""
Suppose there is a volume of 4500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for determining the diameter of a sphere says: Take the volume in cubic chi and multiply it by 16.
Divide the result by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a* chi.
"""

# 積四千五百尺
積 = 4500

# 置積尺數以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方 (cube root)
# To compute the cube root, we raise the value to the power of 1/3.
丸徑 = 積除九 ** Fraction(1, 3)

a = 丸徑
"""
Variable 'a' has wrong value. Expected: 20, Actual: 19.999999999999996"""
