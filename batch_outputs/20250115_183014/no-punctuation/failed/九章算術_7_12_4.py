"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine (醇酒) at 1 dou worth 50 qian, and diluted wine (行酒) at 1 dou worth 10 qian.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine does one obtain?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for excess and deficit says: Place the rates of the items being sold, and the excess and deficit, each below the other.
Multiply the rates of the items being sold, and add them together to form the dividend.
Add the excess and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
For the excess and deficit to balance, place the rates of the items being sold, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend represents the value of the item, and the divisor represents the number of people.

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
醇酒量_假1 = 5  # 醇酒 5 升
行酒量_假1 = 15  # 行酒 1 斗 5 升 (15 升)
盈1 = 10  # 餘 10 錢

# 假令醇酒二升行酒一斗八升不足二
醇酒量_假2 = 2  # 醇酒 2 升
行酒量_假2 = 18  # 行酒 1 斗 8 升 (18 升)
不足2 = -2  # 不足 2 錢

# 盈不足術
# 置所出率盈不足各居其下
實1 = 醇酒量_假1 * 醇酒率 + 行酒量_假1 * 行酒率  # 第一假設的實
實2 = 醇酒量_假2 * 醇酒率 + 行酒量_假2 * 行酒率  # 第二假設的實

# 盈不足相加
盈不足和 = 盈1 + abs(不足2)

# 盈不足相與同其買物者
# 置所出率以少減多餘以約法實
差額 = abs(實1 - 實2)
盈不足和簡化 = 盈不足和

# 實如法而一
醇酒量 = Fraction(差額, 盈不足和簡化)  # 醇酒量
行酒量 = 總酒 - Fraction(醇酒量, 10)  # 行酒量 (總酒 - 醇酒量轉換為斗)

# 答案
a = 醇酒量
b = 行酒量
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 10
Variable 'b' has wrong value. Expected: 7/4, Actual: 1"""
