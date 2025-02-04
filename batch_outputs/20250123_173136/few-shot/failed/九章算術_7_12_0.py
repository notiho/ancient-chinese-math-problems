"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) at 1 dou for 50 qian, and diluted wine (行酒) at 1 dou for 10 qian.
Now, with 30 qian, one obtains 2 dou of wine in total.
Question: how much pure wine and diluted wine does one obtain?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.
The procedure for excess and deficiency (盈不足術) says: Place the prices (rates of exchange) of the goods, and place the excess and deficiency below them respectively.
Multiply the prices by the excess and deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there are fractions, simplify them.
For the goods corresponding to the excess and deficiency, place the prices, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the price of the goods, and the divisor becomes the quantity of people.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# 醇酒一斗，直錢五十
醇酒價 = 50

# 行酒一斗，直錢一十
行酒價 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = 5 / 10  # 5 sheng = 0.5 dou
盈_行酒 = 1.5  # 1 dou 5 sheng = 1.5 dou
盈 = 10  # excess of 10 qian

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = 2 / 10  # 2 sheng = 0.2 dou
不足_行酒 = 1.8  # 1 dou 8 sheng = 1.8 dou
不足 = -2  # deficiency of 2 qian

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 醇酒價 * 盈_醇酒 + 行酒價 * 盈_行酒
不足率 = 醇酒價 * 不足_醇酒 + 行酒價 * 不足_行酒

# 令維乘所出率，并以為實
實 = 盈率 * abs(不足) + 不足率 * abs(盈)

# 并盈、不足為法
法 = abs(盈) + abs(不足)

# 實如法而一
醇酒量 = Fraction(實, 法)

# 醇酒量為 a 升
a = 醇酒量 * 10  # convert dou to sheng

# 行酒量為 b 斗
b = 總酒 - 醇酒量
"""
Code error: both arguments should be Rational instances"""
