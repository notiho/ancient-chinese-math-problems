"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine, 1 dou of which is worth 50 qian, and diluted wine, 1 dou of which is worth 10 qian.
Now, with 30 qian, 2 dou of wine are obtained.
Question: how much pure wine and diluted wine are obtained?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.

The procedure for excess and deficiency says: Place the rates of the goods being sold, and the excess and deficiency, each below the other.
Multiply the rates of the goods being sold by the excess and deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the solution. If there are fractions, simplify them.
If the excess and deficiency are the same, place the rates of the goods being sold, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the value of the goods, and the divisor represents the number of people.

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
假醇酒1 = 5  # 醇酒 5 升
假行酒1 = 1 + Fraction(5, 10)  # 行酒 1 斗 5 升
盈1 = 10  # 錢多 10

# 假令醇酒二升行酒一斗八升不足二
假醇酒2 = 2  # 醇酒 2 升
假行酒2 = 1 + Fraction(8, 10)  # 行酒 1 斗 8 升
不足2 = -2  # 錢少 2

# 盈不足術
# 置所出率盈不足各居其下
實1 = 醇酒率 * 假醇酒1 + 行酒率 * 假行酒1
實2 = 醇酒率 * 假醇酒2 + 行酒率 * 假行酒2

# 盈不足相加為法
法 = 盈1 - 不足2

# 盈不足各乘所出率并以為實
實 = 盈1 * abs(不足2) + abs(盈1) * 不足2

# 實如法而一
醇酒 = Fraction(實, 法)

# 行酒 = 總酒 - 醇酒
行酒 = 總酒 - 醇酒

# Convert 醇酒 to 升 (1 斗 = 10 升)
a = 醇酒 * 10
b = 行酒


"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 0
Variable 'b' has wrong value. Expected: 7/4, Actual: 2"""
