"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
術曰：令兩出門步數相乘，因而四之，為實。開方除之，即得邑方。
荅曰： a里 。
"""

"""

"""

#----- content starts here -----

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
# 邑方 = sqrt(實)，但因無外部函數，需手動計算平方根
# 使用連分數法或牛頓法手動計算平方根
def 開方(n, 精度=10):
    x = n
    for _ in range(精度):
        x = (x + n / x) / 2
    return x

邑方 = 開方(實)

# 轉換為里（1里 = 300步）
a = Fraction(邑方, 300)
#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
