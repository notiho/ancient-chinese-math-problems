"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine, 1 dou of which is worth 50 qian, and diluted wine, 1 dou of which is worth 10 qian.
Now, with 30 qian, 2 dou of wine is obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, with an excess of 10.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, with a deficit of 2.

The procedure for surplus and deficit says: Place the rates of the items being sold, and the surplus and deficit, each below the other.
Multiply the rates of the items being sold by the surplus and deficit, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to find the result.
If there is a fraction, simplify it.
If the surplus and deficit are of the same type, adjust accordingly.
For the items being purchased, place the rates of the items being sold, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the value of the item, and the divisor represents the total number of people.

Answer: *a* sheng of pure wine, *b* dou of diluted wine.
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
盈 = 10  # surplus
不足 = 2  # deficit

# 置所出率盈不足各居其下
醇酒盈 = 醇酒率 * 盈
行酒不足 = 行酒率 * 不足

# 令維乘所出率并以為實
實 = 醇酒盈 + 行酒不足

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
醇酒量 = Fraction(實, 法)

# 醇酒量為醇酒的價值，求醇酒的量
醇酒量 = Fraction(醇酒量, 醇酒率)

# 總酒 - 醇酒量 = 行酒量
行酒量 = 總酒 - 醇酒量

# Convert to appropriate units
a = 醇酒量 * 10  # Convert to sheng
b = 行酒量  # Already in dou
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 26/3
Variable 'b' has wrong value. Expected: 7/4, Actual: 17/15"""
