"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰醇酒 a升 行酒 b斗 
"""

#----- content starts here -----
"""
Suppose there is pure wine, 1 dou of which is worth 50 qian, and diluted wine, 1 dou of which is worth 10 qian.
Now, with 30 qian, 2 dou of wine are to be obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for surplus and deficit says: Place the rates of the goods being sold, and the surplus and deficit, each below the other.
Multiply the rates of the goods being sold, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
If the surplus and deficit are of the same type, adjust accordingly.
For the goods being purchased, place the rates of the goods being sold, subtract the smaller from the larger, and reduce the divisor and dividend accordingly.
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# 醇酒一斗直錢五十
醇酒率 = 50

# 行酒一斗直錢一十
行酒率 = 10

# 錢三十
錢 = 30

# 酒二斗
酒 = 2

# 假令醇酒五升行酒一斗五升有餘一十
盈_醇酒 = 5
盈_行酒 = 1 + Fraction(5, 10)
盈 = 10

# 假令醇酒二升行酒一斗八升不足二
不足_醇酒 = 2
不足_行酒 = 1 + Fraction(8, 10)
不足 = -2

# 盈不足術：置所出率盈不足各居其下
盈_率 = 醇酒率 * 盈_醇酒 + 行酒率 * 盈_行酒
不足_率 = 醇酒率 * 不足_醇酒 + 行酒率 * 不足_行酒

# 盈不足相加為法
法 = 盈 - 不足

# 盈不足各乘所出率并以為實
實 = 盈_率 - 不足_率

# 實如法而一
單位 = Fraction(實, 法)

# 醇酒 a升
a = 單位 * 盈_醇酒

# 行酒 b斗
b = 單位 * 盈_行酒#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 245/4
Variable 'b' has wrong value. Expected: 7/4, Actual: 147/8"""
