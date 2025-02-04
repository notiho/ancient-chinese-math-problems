"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) worth 50 qian per dou, and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, with an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, with a deficit of 2 qian.
The "excess and deficit" procedure says: Place the rates of output (prices) with the excess and deficit below them, respectively.
Multiply the rates of output by the excess and deficit, summing them to form the dividend.
Sum the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there are fractions, simplify them.
For the excess and deficit, adjust the result to match the item being purchased.
Place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

from fractions import Fraction

# Prices of pure wine and diluted wine per dou
醇酒價 = 50
行酒價 = 10

# Total money and total wine
總錢 = 30
總酒 = 2  # in dou

# Excess and deficit cases
# Case 1: 5 sheng of pure wine, 1 dou 5 sheng of diluted wine, excess of 10 qian
醇酒量1 = Fraction(5, 10)  # 5 sheng = 0.5 dou
行酒量1 = Fraction(1, 1) + Fraction(5, 10)  # 1.5 dou
盈1 = 10

# Case 2: 2 sheng of pure wine, 1 dou 8 sheng of diluted wine, deficit of 2 qian
醇酒量2 = Fraction(2, 10)  # 2 sheng = 0.2 dou
行酒量2 = Fraction(1, 1) + Fraction(8, 10)  # 1.8 dou
不足2 = 2

# 盈不足術
# Multiply rates of output by excess and deficit, summing them to form the dividend
實 = (醇酒量1 * 盈1 + 醇酒量2 * 不足2)

# Sum the excess and deficit to form the divisor
法 = (盈1#----- content ends here -----

"""
Code error: '(' was never closed (<string>, line 47)"""
