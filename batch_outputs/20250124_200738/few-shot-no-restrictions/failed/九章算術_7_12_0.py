"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) worth 50 qian per dou and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.

The method of surplus and deficiency (盈不足術) says: Place the unit prices (所出率) of the two types of wine, and place the surplus (盈) and deficiency (不足) below them respectively.
Multiply the unit prices by the surplus and deficiency, sum them to form the dividend (實).
Sum the surplus and deficiency to form the divisor (法).
Divide the dividend by the divisor to obtain the result.
If there is a remainder, simplify it.
For the surplus and deficiency corresponding to the same item being purchased, place the unit prices, subtract the smaller from the larger, and simplify the remainder with the divisor and dividend.
The dividend represents the price of the item, and the divisor represents the total quantity.

Answer: *a* sheng of pure wine and *b* dou of diluted wine.
"""

from fractions import Fraction

# 醇酒一斗，直錢五十
醇酒價 = 50

# 行酒一斗，直錢一十
行酒價 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 假設盈不足情況
盈 = 10  # 餘一十
不足 = 2  # 不足二

# 置所出率
醇酒率 = 醇酒價
行酒率 = 行酒價

# 盈不足術計算
實 = 盈 * 行酒率 + 不足 * 醇酒率  # 實
法 = 盈 + 不足  # 法

# 實如法而一
醇酒量 = Fraction(實, 法)  # 醇酒量 in qian

# 醇酒量轉換為升
醇酒量升 = Fraction(醇酒量, 醇酒價) * 10  # 1斗 = 10升

# 行酒量
行酒量升 = 總酒 * 10 - 醇酒量升  # 總酒量 - 醇酒量

# 結果
a = 醇酒量升  # 醇酒量 in 升
b = Fraction(行酒量升, 10)  # 行酒量 in 斗

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 10/3
Variable 'b' has wrong value. Expected: 7/4, Actual: 5/3"""
