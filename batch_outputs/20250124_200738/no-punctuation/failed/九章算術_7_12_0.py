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
Question: how much pure wine and how much diluted wine are obtained?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for excess and deficit says: Place the rates of the outputs, and the excess and deficit, each below the other.
Multiply the rates of the outputs by the excess and deficit, and add them together to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there are fractions, simplify them.
If the excess and deficit are of the same type, adjust accordingly.
For the items being purchased, place the rates of the outputs, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

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
醇酒假1 = 5  # 醇酒 5 升
行酒假1 = 1 + Fraction(5, 10)  # 行酒 1 斗 5 升
盈1 = 10  # 餘 10 錢

# 假令醇酒二升行酒一斗八升不足二
醇酒假2 = 2  # 醇酒 2 升
行酒假2 = 1 + Fraction(8, 10)  # 行酒 1 斗 8 升
不足2 = -2  # 不足 2 錢

# 盈不足術
# 置所出率盈不足各居其下
實1 = 醇酒假1 * 醇酒率 + 行酒假1 * 行酒率
實2 = 醇酒假2 * 醇酒率 + 行酒假2 * 行酒率

# 盈不足相加為法
法 = 盈1 - 不足2

# 實如法而一
醇酒份額 = Fraction(實1 - 實2, 法)

# 醇酒 a 升
a = 醇酒份額

# 行酒 b 斗
b = 總酒 - Fraction(a, 10)  # 總酒減去醇酒的斗數

#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 49/4
Variable 'b' has wrong value. Expected: 7/4, Actual: 31/40"""
