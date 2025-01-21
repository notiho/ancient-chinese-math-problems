"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

"""
Suppose there is pure wine, one dou of which costs 50 qian, and diluted wine, one dou of which costs 10 qian.
Now, with 30 qian, 2 dou of wine are obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.

The procedure for surplus and deficit says: Place the rates of the items being sold, with the surplus and deficit below each.
Multiply the rates by the surplus and deficit, respectively, and add them to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For the surplus and deficit corresponding to the same item being purchased, place the rates, subtract the smaller from the larger, and reduce the remainder with the divisor and dividend.
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a*(=5/2) sheng of pure wine, *b*(=7/4) dou of diluted wine.
"""

# 醇酒一斗，直錢五十
醇酒率 = 50

# 行酒一斗，直錢一十
行酒率 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 盈不足術
# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = 5 / 10  # 5 sheng = 5/10 dou
盈_行酒 = 1 + 5 / 10  # 1 dou 5 sheng = 1.5 dou
盈 = 10  # surplus of 10 qian

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = 2 / 10  # 2 sheng = 2/10 dou
不足_行酒 = 1 + 8 / 10  # 1 dou 8 sheng = 1.8 dou
不足 = -2  # deficit of 2 qian

# 置所出率，盈、不足各居其下
盈實 = (醇酒率 * 盈_醇酒 + 行酒率 * 盈_行酒) * 盈
不足實 = (醇酒率 * 不足_醇酒 + 行酒率 * 不足_行酒) * abs(不足)

# 并以為實
實 = 盈實 + 不足實

# 并盈、不足為法
法 = 盈 + abs(不足)

# 實如法而一
醇酒量 = Fraction(盈_醇酒 * 盈 + 不足_醇酒 * abs(不足), 法)
行酒量 = Fraction(盈_行酒 * 盈 + 不足_行酒 * abs(不足), 法)

# Convert to appropriate units
a = 醇酒量 * 10  # Convert to sheng (5/2 sheng)
b = 行酒量  # Already in dou (7/4 dou)
"""
Code error: both arguments should be Rational instances"""
