"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,644,864,437,500 cubic chi.
Question: what is the diameter of the sphere?

The procedure for finding the diameter of a sphere says:
Take the volume in cubic chi, multiply it by 16, and divide it by 9.
Then take the cube root of the result, which gives the diameter of the sphere.

Answer: *a* chi.
"""

from fractions import Fraction
import math

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積 = 1644864437500

# 以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方
開立方 = 積除九 ** Fraction(1, 3)

# 即丸徑
a = float(開立方)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14300, Actual: 14299.994204187651"""
