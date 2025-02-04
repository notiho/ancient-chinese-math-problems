"""
今有共買璡人出半盈四人出少半不足三問人數璡價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 璡價 b 
"""

"""
Suppose a group of people jointly buys a jade object. 
One person contributes half the price and has 4 units in excess.
The remaining people each contribute less than half the price, and together they are short by 3 units.
Question: how many people are there, and what is the price of the jade object?

The procedure for "Excess and Deficit" says:
Place the contribution rates, with the excess and deficit each below them.
Let the contributions multiply their respective rates, and sum them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain 1. If there is a fraction, reduce it.
The excess and deficit are treated equally.
For the buyers, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend gives the price of the object, and the divisor gives the number of people.

Answer: *a* people, jade price *b*.
"""

from fractions import Fraction

# One person contributes half the price and has 4 units in excess.
多率 = Fraction(1, 2)
多盈 = 4

# The remaining people each contribute less than half the price, and together they are short by 3 units.
少率 = Fraction(1, 2)
少不足 = 3

# 置所出率，盈不足各居其下
# Let the contributions multiply their respective rates, and sum them to form the dividend.
實 = (多率 * 多盈) + (少率 * 少不足)

# 并盈不足為法
法 = 多盈 + 少不足

# 實如法而一，有分者通之
物價 = Fraction(實, 法)

# 盈不足相與同，其買物者置所出率，以少減多，餘以約法實
人數 = Fraction(多盈 - 少不足, 法)

# 實為物價，法為人數
a = 人數
b = 物價
"""
Variable 'a' has wrong value. Expected: 42, Actual: 1/7
Variable 'b' has wrong value. Expected: 17, Actual: 1/2"""
