"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine, 1 dou of which is worth 50 qian, and diluted wine, 1 dou of which is worth 10 qian.
Now, with 30 qian, 2 dou of wine are obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for surplus and deficit says: Place the rates of output, surplus, and deficit below each other.
Multiply the rates of output by their corresponding surplus or deficit, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result.
If there are fractions, simplify them.
If the surplus and deficit are of the same type, adjust accordingly.
For the item being purchased, place the rates of output, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* sheng of pure wine and *b* dou of diluted wine.
"""

# 醇酒一斗直錢五十
醇酒率 = 50

# 行酒一斗直錢一十
行酒率 = 10

# 錢三十得酒二斗
總錢 = 30
總酒 = 2

# 假令醇酒五升行酒一斗五升有餘一十
醇酒_假1 = 5
行酒_假1 = 1 + Fraction(5, 10)
盈1 = 10

# 假令醇酒二升行酒一斗八升不足二
醇酒_假2 = 2
行酒_假2 = 1 + Fraction(8, 10)
不足2 = -2

# 盈不足術
# 置所出率盈不足各居其下
實1 = 醇酒_假1 * 盈1 + 行酒_假1 * 盈1
實2 = 醇酒_假2 * 不足2 + 行酒_假2 * 不足2

# 并盈不足為法
法 = 盈1 + abs(不足2)

# 實如法而一
醇酒比例 = Fraction(實1, 法)
行酒比例 = Fraction(實2, 法)

# 醇酒 a升
a = 醇酒比例 * 總酒

# 行酒 b斗
b = 行酒比例 * 總酒
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 65/6
Variable 'b' has wrong value. Expected: 7/4, Actual: -19/15"""
