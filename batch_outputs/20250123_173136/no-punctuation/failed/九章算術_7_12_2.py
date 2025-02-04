"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine (醇酒) worth 50 qian per dou and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, 2 dou of wine is obtained.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine are obtained, leaving an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine are obtained, falling short by 2 qian.

The procedure for surplus and deficit (盈不足術) says: Place the rates of output (所出率), surplus (盈), and deficit (不足) below each other.
Multiply the rates of output by the surplus and deficit, respectively, and sum them to form the dividend (實).
Sum the surplus and deficit to form the divisor (法).
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
If the surplus and deficit are related to the same item being purchased, place the rates of output, subtract the smaller from the larger, and reduce the divisor and dividend accordingly.
The dividend represents the value of the item, and the divisor represents the number of people.

Answer: *a* sheng of pure wine and *b* dou of diluted wine.
"""

# 醇酒一斗直錢五十
醇酒價 = 50

# 行酒一斗直錢一十
行酒價 = 10

# 錢三十
總錢 = 30

# 酒二斗
總酒 = 2

# 假令醇酒五升行酒一斗五升有餘一十
醇酒率1 = 5  # 醇酒 5 升
行酒率1 = 1 + Fraction(5, 10)  # 行酒 1 斗 5 升
盈 = 10  # 餘 10 錢

# 假令醇酒二升行酒一斗八升不足二
醇酒率2 = 2  # 醇酒 2 升
行酒率2 = 1 + Fraction(8, 10)  # 行酒 1 斗 8 升
不足 = 2  # 不足 2 錢

# 盈不足術
# 置所出率盈不足各居其下
實 = (醇酒率1 * 不足) + (醇酒率2 * 盈)  # 實
法 = 盈 + 不足  # 法

# 實如法而一
醇酒量 = Fraction(實, 法)

# 行酒量
行酒量 = 總酒 - 醇酒量

# 將醇酒量轉換為升
a = 醇酒量 * 10  # 醇酒量以升表示
b = 行酒量  # 行酒量以斗表示
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 25
Variable 'b' has wrong value. Expected: 7/4, Actual: -1/2"""
