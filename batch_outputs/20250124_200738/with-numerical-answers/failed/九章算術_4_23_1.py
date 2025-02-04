"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a(=14300)尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,644,864,437,500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says: Place the volume in cubic chi.
Multiply it by 16.
Divide it by 9.
Take the cube root of the result, and that is the diameter of the sphere.

Answer: *a*(=14300) chi.
"""

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積 = 1644864437500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方除之，即丸徑
# Since we cannot use external libraries, we manually compute the cube root through approximation.
def cube_root(n):
    x = n
    while True:
        next_x = (2 * x + n / (x * x)) / 3
        if abs(next_x - x) < Fraction(1, 10**10):  # Precision threshold
            return next_x
        x = next_x

a = int(cube_root(積除九))  # 14300 chi#----- content ends here -----

"""
Timed out"""
