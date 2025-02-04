"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
開立圓術曰：置積尺數，以十六乘之，九而一，所得開立方除之，即丸徑。
荅曰： a尺 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 積一萬六千四百四十八億六千六百四十三萬七千五百尺
積 = 164486437500

# 置積尺數，以十六乘之
積乘十六 = 16 * 積

# 九而一
積開立方 = Fraction(積乘十六, 9)

# 開立方 (即取立方根)
# 我們需要手動計算立方根，這裡使用近似方法
def 立方根(x):
    guess = x / 3
    for _ in range(20):  # 迭代逼近
        guess = (2 * guess + x / (guess * guess)) / 3
    return guess

# 所得開立方除之，即丸徑
a = 立方根(積開立方)

# 答案
a
#----- content ends here -----


"""

"""


"""
Timed out"""
