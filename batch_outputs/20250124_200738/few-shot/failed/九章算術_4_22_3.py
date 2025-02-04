"""
今有積四千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 4500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says: Take the volume in cubic chi, multiply it by 16.
Divide the result by 9, then take the cube root of the result to find the diameter of the sphere.

Answer: the diameter is *a* chi.
"""

# 積四千五百尺
積 = 4500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# To compute the cube root, we use exponentiation with Fraction(1, 3)
a = 積除九 ** Fraction(1, 3)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 20, Actual: 19.999999999999996"""
