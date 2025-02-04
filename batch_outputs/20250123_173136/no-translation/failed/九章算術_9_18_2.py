"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""

"""


from fractions import Fraction

# 出北門三十步有木
北門步數 = 30

# 出西門七百五十步見木
西門步數 = 750

# 令兩出門步數相乘
實 = 北門步數 * 西門步數

# 因而四之
實 *= 4

# 開方除之，即得邑方
# 開方即平方根，邑方為實的平方根
# 由於 Python 無法直接用內建函數處理開方，這裡手動計算平方根
def 開方(數):
    x = Fraction(數)
    y = Fraction(1)
    while abs(x - y) > Fraction(1, 1000000):  # 精度控制
        x = (x + y) / 2
        y = 數 / x
    return x

邑方 = 開方(實)

# 1 里 = 300 步
a = Fraction(邑方, 300)


"""

"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: Too large to be printed"""
