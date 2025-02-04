"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,644,864,437,500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says: Place the volume in cubic chi.
Multiply it by 16.
Divide it by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a* chi.
"""

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積 = 1644864437500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# To compute the cube root manually without external libraries:
def cube_root(n):
    # Use binary search to approximate the cube root
    low = 0
    high = n
    while high - low > Fraction(1, 10**10):  # Precision to 10 decimal places
        mid = (low + high) / 2
        if mid**3 < n:
            low = mid
        else:
            high = mid
    return (low + high) / 2

a = cube_root(積除九)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14300, Actual: 16882453333771533787296875/1180591620717411303424"""
