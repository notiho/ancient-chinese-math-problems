"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

"""
Suppose there is pure wine (醇酒) priced at 50 qian per dou, and diluted wine (行酒) priced at 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2.
The procedure for surplus and deficit (盈不足術) says: Place the rates of output, with surplus and deficit below each.
Multiply the rates of output by their respective surplus or deficit, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to obtain the result. If there are fractions, simplify them.
For surplus and deficit problems involving the same goods, place the rates of output, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend represents the value of the goods, and the divisor represents the number of people.

Answer: *a*(=5/2) sheng of pure wine, and *b*(=7/4) dou of diluted wine.
"""

from fractions import Fraction

# 醇酒一斗，直錢五十
醇酒價 = 50

# 行酒一斗，直錢一十
行酒價 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 盈不足術
# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = Fraction(5, 10)  # 5 sheng = 0.5 dou
盈_行酒 = Fraction(15, 10)  # 1 dou 5 sheng = 1.5 dou
盈 = 10  # surplus

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = Fraction(2, 10)  # 2 sheng = 0.2 dou
不足_行酒 = Fraction(18, 10)  # 1 dou 8 sheng = 1.8 dou
不足 = 2  # deficit

# 置所出率，盈、不足各居其下
盈率 = 盈_醇酒 * 醇酒價 + 盈_行酒 * 行酒價
不足率 = 不足_醇酒 * 醇酒價 + 不足_行酒 * 行酒價

# 令維乘所出率，并以為實
實 = 盈率 * 不足 + 不足率 * 盈

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
醇酒量 = Fraction(實, 法) / 醇酒價  # in dou
行酒量 = 總酒 - 醇酒量  # in dou

# Convert to required units
a = 醇酒量 * 10  # Convert to sheng (5/2 sheng)
b = 行酒量  # Already in dou (7/4 dou)
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 6
Variable 'b' has wrong value. Expected: 7/4, Actual: 7/5"""
