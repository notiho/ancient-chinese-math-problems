"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""

"""


from fractions import Fraction

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積尺數 = 1644866437500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積尺數

# 九而一
積開立方 = Fraction(積乘十六, 9)

# 開立方 (即立方根)
# Since Python does not have a direct method for exact cube roots, we approximate:
丸徑 = 積開立方 ** Fraction(1, 3)

a = 丸徑


"""
 

This code calculates the diameter of a sphere given its volume using the ancient Chinese method described. Note that the cube root is approximated here, as Python's `Fraction` does not support exact cube root calculations.
"""


"""
Variable 'a' has wrong value. Expected: 14300, Actual: 14299.999999999993"""
