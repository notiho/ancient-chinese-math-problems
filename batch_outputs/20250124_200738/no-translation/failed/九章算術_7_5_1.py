"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 人出五，不足四十五
出率1 = 5
不足1 = 45

# 人出七，不足三
出率2 = 7
不足2 = 3

# 令維乘所出率，以少減多，餘為實
實 = (不足1 * 出率2) - (不足2 * 出率1)

# 兩盈、兩不足以少減多，餘為法
法 = (出率2 - 出率1)

# 實如法而一
人數 = Fraction(實, 法)

# 羊價
羊價 = 出率1 * 人數 + 不足1

a = 人數
b = 羊價
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 21, Actual: 150
Variable 'b' has wrong value. Expected: 150, Actual: 795"""
