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
# 開方即取平方根，平方根的分數形式可以表示為分母和分子平方根的比值
# 這裡我們用分數表示結果
a = Fraction(實).limit_denominator().sqrt()
#----- content ends here -----


"""

"""


"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
