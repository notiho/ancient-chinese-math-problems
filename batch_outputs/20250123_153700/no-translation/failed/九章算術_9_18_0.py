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
實 = 4 * 實

# 開方除之，即得邑方
# 開方即為平方根，邑方為平方根的結果
# 邑方 = sqrt(實)
# 但 Python 中無法直接使用開方運算，需手動模擬開方
def 開方(數):
    # 模擬開方運算，逐步逼近
    x = Fraction(數, 2)  # 初始猜測值
    while True:
        next_x = Fraction(x + 數 / x, 2)
        if abs(next_x - x) < Fraction(1, 1000000):  # 精度控制
            return next_x
        x = next_x

邑方 = 開方(實)

# 轉換為里（1里 = 300步）
a = Fraction(邑方, 300)


"""

"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: Too large to be printed"""
