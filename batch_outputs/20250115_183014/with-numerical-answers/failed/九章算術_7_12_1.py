"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

"""
Suppose there is pure wine (醇酒) at 1 dou costing 50 qian, and diluted wine (行酒) at 1 dou costing 10 qian.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine does one get?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, leaving a deficit of 2.

The procedure for excess and deficit says: Place the rates of the items being sold, with the excess and deficit below them respectively.
Multiply the rates by the excess and deficit, and add them together to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
For the excess and deficit corresponding to the same item being purchased, place the rates of the items being sold, subtract the smaller from the larger, and simplify the remainder with the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=5/2) sheng of pure wine, and *b*(=7/4) dou of diluted wine.
"""

# 醇酒一斗，直錢五十
醇酒率 = 50

# 行酒一斗，直錢一十
行酒率 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2

# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = Fraction(5, 10)  # 5升 = 5/10斗
盈_行酒 = Fraction(15, 10)  # 1斗5升 = 15/10斗
盈 = 10

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = Fraction(2, 10)  # 2升 = 2/10斗
不足_行酒 = Fraction(18, 10)  # 1斗8升 = 18/10斗
不足 = -2

# 盈不足術
# 置所出率，盈、不足各居其下
盈實 = (醇酒率 * 盈_醇酒) + (行酒率 * 盈_行酒)
不足實 = (醇酒率 * 不足_醇酒) + (行酒率 * 不足_行酒)

# 令維乘所出率，并以為實
實 = (盈 * 不足實) - (不足 * 盈實)

# 并盈、不足為法
法 = 盈 - 不足

# 實如法而一
醇酒 = Fraction(實, 法)

# 醇酒 a(=5/2)升
a = 醇酒  # 5/2斗

# 行酒 b(=7/4)斗
行酒 = 總酒 - 醇酒
b = 行酒  # 7/4斗
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 30
Variable 'b' has wrong value. Expected: 7/4, Actual: -28"""
