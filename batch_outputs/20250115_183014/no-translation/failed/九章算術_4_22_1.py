"""
今有積四千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""

"""


from fractions import Fraction

# 積四千五百尺
積 = 4500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積除九 = Fraction(積乘十六, 9)

# 所得開立方
# Note: To "開立方" (cube root), we raise the value to the power of 1/3
開立方 = 積除九 ** Fraction(1, 3)

# 除之，即丸徑
a = 開立方

# Answer
a  # 丸徑 in 尺


"""

"""


"""
Variable 'a' has wrong value. Expected: 20, Actual: 19.999999999999996"""
