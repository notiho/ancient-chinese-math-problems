"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine, 1 dou of which is worth 50 qian, and diluted wine, 1 dou of which is worth 10 qian.
Now, with 30 qian, 2 dou of wine are to be obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for surplus and deficit says: Place the rates of exchange for the goods under the surplus and deficit respectively.
Multiply the rates of exchange by the surplus and deficit, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there are fractions, simplify them.
If the surplus and deficit are related to the same goods, place the rates of exchange, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# 醇酒一斗直錢五十
醇酒率 = 50

# 行酒一斗直錢一十
行酒率 = 10

# 錢三十
總錢 = 30

# 酒二斗
總酒 = 2

# 盈不足術
# 假令醇酒五升行酒一斗五升有餘一十
盈_醇酒 = 5
盈_行酒 = 1 + Fraction(5, 10)
盈 = 10

# 假令醇酒二升行酒一斗八升不足二
不足_醇酒 = 2
不足_行酒 = 1 + Fraction(8, 10)
不足 = 2

# 置所出率盈不足各居其下
盈率 = 醇酒率 * 盈_醇酒 + 行酒率 * 盈_行酒
不足率 = 醇酒率 * 不足_醇酒 + 行酒率 * 不足_行酒

# 令維乘所出率并以為實
實 = 盈率 * 不足 + 不足率 * 盈

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
醇酒份額 = Fraction(實, 法)

# 醇酒 a升
a = Fraction(醇酒份額, 醇酒率)

# 行酒 b斗
b = 總酒 - a
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 57/20
Variable 'b' has wrong value. Expected: 7/4, Actual: -17/20"""
