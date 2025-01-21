"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) worth 50 qian per dou and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2.

The procedure for excess and deficiency (盈不足術) says:
Place the rates of the goods (所出率), with the excess (盈) and deficiency (不足) below them respectively.
Multiply the rates by the excess and deficiency, and sum them to form the dividend (實).
Sum the excess and deficiency to form the divisor (法).
Divide the dividend by the divisor to find the result.
If there is a remainder, adjust it proportionally.
For the goods corresponding to the excess and deficiency, place their rates, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.
The dividend becomes the price of the goods, and the divisor becomes the number of people.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# 醇酒一斗，直錢五十
醇酒率 = 50

# 行酒一斗，直錢一十
行酒率 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = 5  # in sheng
盈_行酒 = 1 * 10 + 5  # in sheng (1 dou 5 sheng = 15 sheng)
盈 = 10  # excess

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = 2  # in sheng
不足_行酒 = 1 * 10 + 8  # in sheng (1 dou 8 sheng = 18 sheng)
不足 = -2  # deficiency

# 盈不足術
# 置所出率，盈、不足各居其下
盈實 = 盈 * 不足_行酒
不足實 = abs(不足) * 盈_行酒

# 令維乘所出率，并以為實
實 = 盈實 + 不足實

# 并盈、不足為法
法 = 盈 + abs(不足)

# 實如法而一
醇酒量 = Fraction(實, 法)

# 醇酒量為 a 升
a = 醇酒量

# 總酒量 - 醇酒量 = 行酒量
行酒量 = 總酒 * 10 - 醇酒量  # Convert total wine to sheng for consistency

# 行酒量為 b 斗
b = Fraction(行酒量, 10)  # Convert back to dou
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 35/2
Variable 'b' has wrong value. Expected: 7/4, Actual: 1/4"""
