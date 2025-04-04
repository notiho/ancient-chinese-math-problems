"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

"""

"""


from fractions import Fraction

# 人出九，盈十一
出率1 = 9
盈 = 11

# 人出六，不足十六
出率2 = 6
不足 = 16

# 令維乘所出率，并以為實
實 = 出率1 * 不足 + 出率2 * 盈

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一。有分者，通之
人數 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘
物價 = 出率1 - 出率2

# 以約法、實
物價 = Fraction(物價 * 人數, 出率1)

# 實為物價，法為人數
a = int(人數)
b = int(物價)


"""

"""


"""
Variable 'a' has wrong value. Expected: 9, Actual: 7
Variable 'b' has wrong value. Expected: 70, Actual: 2"""
