"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 盈不足術
# 盈四
盈 = 4

# 不足三
不足 = 3

# 人出半
所出率多 = Fraction(1, 2)

# 人出少半
所出率少 = Fraction(1, 4)

# 置所出率，盈、不足各居其下
# 令維乘所出率，并以為實
實 = 盈 * 所出率少 + 不足 * 所出率多

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一。有分者，通之
人數 = Fraction(實, 法)

# 盈不足相與同其買物者
# 置所出率，以少減多，餘，以約法、實
物價 = Fraction(所出率多 - 所出率少, 法) * 實

# 答案
a = int(人數)
b = int(物價)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 42, Actual: 0
Variable 'b' has wrong value. Expected: 17, Actual: 0"""
