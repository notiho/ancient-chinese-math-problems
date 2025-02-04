"""
今有積三百步。問︰為圓周幾何？
開圓術曰：置積步數，以十二乘之，以開方除之，即得周。
荅曰： a步 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 積三百步
積步數 = 300

# 置積步數，以十二乘之
積乘十二 = 12 * 積步數

# 開方除之，即得周
# 開方的結果是平方根，手動計算開方
def 開方(n):
    x = n
    y = (x + n / x) / 2
    while abs(x - y) > Fraction(1, 1000000):  # 精度控制
        x = y
        y = (x + n / x) / 2
    return x

周 = 開方(積乘十二)

a = 周
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 60, Actual: 60.000000000000185"""
