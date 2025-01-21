"""
今有醇酒一斗直錢五十行酒一斗直錢一十今將錢三十得酒二斗問醇行酒各得幾何
術曰假令醇酒五升行酒一斗五升有餘一十令之醇酒二升行酒一斗八升不足二
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰醇酒 a升 行酒 b斗 
"""

"""
Suppose there is pure wine (醇酒) costing 50 qian per dou and diluted wine (行酒) costing 10 qian per dou.
Now, with 30 qian, it is desired to obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose 5 sheng of pure wine and 1 dou 5 sheng of diluted wine result in an excess of 10 qian.
Suppose 2 sheng of pure wine and 1 dou 8 sheng of diluted wine result in a deficit of 2 qian.

The procedure for surplus and deficit (盈不足術) says: Place the rates of the outputs (所出率) and the surplus and deficit (盈不足) below them.
Multiply the rates of the outputs by the surplus and deficit, add them together to form the dividend (實).
Add the surplus and deficit together to form the divisor (法).
Divide the dividend by the divisor, and if there is a remainder, adjust it proportionally.
If the surplus and deficit are of the same type, adjust accordingly.
For the purchased items, place the rates of the outputs, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
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
盈_醇酒 = 5
盈_行酒 = 1 + Fraction(5, 10)
盈 = 10

# 假令醇酒二升行酒一斗八升不足二
不足_醇酒 = 2
不足_行酒 = 1 + Fraction(8, 10)
不足 = -2

# 盈不足術
# 置所出率盈不足各居其下
盈實 = 盈_醇酒 * 盈 + 盈_行酒 * 盈
不足實 = 不足_醇酒 * 不足 + 不足_行酒 * 不足

# 令維乘所出率并以為實
實 = 盈實 + 不足實

# 并盈不足為法
法 = 盈 + abs(不足)

# 實如法而一
醇酒份 = Fraction(實, 法)

# 醇酒 a升
a = 醇酒份

# 行酒 b斗
b = 總酒 - Fraction(a, 10)  # Convert a (sheng) to dou and subtract from total wine
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 287/60
Variable 'b' has wrong value. Expected: 7/4, Actual: 913/600"""
