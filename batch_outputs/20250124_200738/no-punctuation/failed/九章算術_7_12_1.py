"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰醇酒 a升 行酒 b斗 
"""

#----- content starts here -----
"""
Suppose there is pure wine, 1 dou of which costs 50 qian, and diluted wine, 1 dou of which costs 10 qian.
Now, with 30 qian, 2 dou of wine are to be obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for surplus and deficit says: Place the rates of the goods being sold, and the surplus and deficit, each below the other.
Multiply the rates of the goods being sold by the surplus and deficit, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
If the surplus and deficit are equal, place the rates of the goods being sold, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the price of the goods, and the divisor represents the quantity of people.

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

# 假令醇酒五升行酒一斗五升有餘一十
盈1 = 10
醇酒量1 = Fraction(5, 10)  # 5升 = 0.5斗
行酒量1 = 1 + Fraction(5, 10)  # 1斗5升 = 1.5斗

# 假令醇酒二升行酒一斗八升不足二
不足2 = -2
醇酒量2 = Fraction(2, 10)  # 2升 = 0.2斗
行酒量2 = 1 + Fraction(8, 10)  # 1斗8升 = 1.8斗

# 盈不足術
# 置所出率盈不足各居其下
實1 = 醇酒率 * 醇酒量1 + 行酒率 * 行酒量1
實2 = 醇酒率 * 醇酒量2 + 行酒率 * 行酒量2

# 盈不足相加為法
法 = 盈1 - 不足2

# 實如法而一
實 = (實1 * abs(不足2) + 實2 * abs(盈1))

# 醇酒量
醇酒量 = Fraction(實, 法)

# 行酒量
行酒量 = 總酒 - 醇酒量

# Convert to appropriate units
a = 醇酒量 * 10  # Convert to 升
b = 行酒量  # In 斗#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 300
Variable 'b' has wrong value. Expected: 7/4, Actual: -28"""
