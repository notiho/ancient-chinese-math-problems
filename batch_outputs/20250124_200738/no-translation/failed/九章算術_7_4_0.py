"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 人出四百，盈三千四百
出率1 = 400
盈1 = 3400

# 人出三百，盈一百
出率2 = 300
盈2 = 100

# 置所出率，盈、不足各居其下
# 令維乘所出率，以少減多，餘為實
實 = (出率1 * 盈2) - (出率2 * 盈1)

# 兩盈、兩不足以少減多，餘為法
法 = 盈2 - 盈1

# 實如法而一
人數 = Fraction(實, 法)

# 金價
金價 = 出率1 * 人數 - 盈1

# 有分者通之
a = 人數
b = 金價
#----- content ends here -----


"""
 

This code follows the ancient Chinese mathematical procedure to calculate the number of people (`a`) and the price of gold (`b`).
"""


"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800/33
Variable 'b' has wrong value. Expected: 9800, Actual: 3807800/33"""
