"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

"""
Suppose there is pure wine (醇酒) costing 50 qian per dou, and diluted wine (行酒) costing 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine does one obtain respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving 10 qian extra.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.
The procedure for surplus and deficit (盈不足術) says: Place the respective rates of the items, with surplus and deficit below them.
Multiply the rates by the surplus and deficit, respectively, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the unit amount. If there is a fraction, simplify it.
For the surplus and deficit, if they correspond to the same item, place the rates, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the price of the item, and the divisor becomes the quantity of people.

Answer: *a*(=5/2) sheng of pure wine, and *b*(=7/4) dou of diluted wine.
"""

from fractions import Fraction

# 醇酒每斗價格
醇酒價格 = 50

# 行酒每斗價格
行酒價格 = 10

# 總錢數
總錢 = 30

# 總酒量
總酒量 = 2  # 2斗

# 盈不足術
# 假設盈不足的數據：
盈 = 10  # 盈餘10錢
不足 = 2  # 不足2錢

# 醇酒與行酒的價格比率
醇酒率 = 50
行酒率 = 10

# 令維乘所出率，并以為實
實 = 盈 * 行酒率 + 不足 * 醇酒率

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
單位量 = Fraction(實, 法)

# 醇酒的量
醇酒量 = Fraction(盈, 法) * 總酒量

# 行酒的量
行酒量 = Fraction(不足, 法) * 總酒量

# 答案
a = 醇酒量  # 5/2 斗
b = 行酒量  # 7/4 斗
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 5/3
Variable 'b' has wrong value. Expected: 7/4, Actual: 1/3"""
