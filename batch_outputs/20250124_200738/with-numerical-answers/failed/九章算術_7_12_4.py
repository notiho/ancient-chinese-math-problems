"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) costing 50 qian per dou, and diluted wine (行酒) costing 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine does one obtain respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving 10 qian extra.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, lacking 2 qian.
The "excess and deficiency" (盈不足) procedure says: Place the rates of the items being purchased, with the excess and deficiency below each.
Multiply the rates by the excess and deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fractional part, simplify it.
For the excess and deficiency, if they correspond to the same item being purchased, place the rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=5/2) dou of pure wine, and *b*(=7/4) dou of diluted wine.
"""

from fractions import Fraction

# 醇酒一斗，直錢五十
醇酒率 = 50

# 行酒一斗，直錢一十
行酒率 = 10

# 錢三十
總錢 = 30

# 酒二斗
總酒 = 2

# 盈不足術
# 假令醇酒五升，行酒一斗五升，有餘一十
盈 = 10
醇酒假1 = Fraction(5, 10)  # 5升 = 5/10斗
行酒假1 = Fraction(15, 10)  # 1斗5升 = 15/10斗

# 令之醇酒二升，行酒一斗八升，不足二
不足 = -2
醇酒假2 = Fraction(2, 10)  # 2升 = 2/10斗
行酒假2 = Fraction(18, 10)  # 1斗8升 = 18/10斗

# 置所出率，盈、不足各居其下
# 醇酒率 = 50, 行酒率 = 10
# 盈 = 10, 不足 = -2

# 令維乘所出率，并以為實
實 = (醇酒率 * 盈) + (醇酒率 * 不足)

# 并盈、不足為法
法 = 盈 - 不足

# 實如法而一
醇酒 = Fraction(實,法#----- content ends here -----

"""
Code error: '(' was never closed (<string>, line 56)"""
