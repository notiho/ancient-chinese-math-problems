"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

"""
Suppose there is pure wine (醇酒) priced at 50 qian per dou, and diluted wine (行酒) priced at 10 qian per dou.
Now, with 30 qian, 2 dou of wine is obtained in total.
Question: how much pure wine and diluted wine is obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.
The procedure for surplus and deficit (盈不足術) says: Place the rates of the items, with surplus and deficit below each.
Multiply the rates by their respective surplus or deficit, and sum them to form the dividend (實).
Sum the surplus and deficit to form the divisor (法).
Divide the dividend by the divisor to find the unit amount. If there is a remainder, adjust accordingly.
For surplus and deficit problems involving the same item, place the rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the item, and the divisor represents the quantity.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

# 醇酒價錢與行酒價錢
醇酒價 = 50  # 錢/斗
行酒價 = 10  # 錢/斗

# 錢三十，得酒二斗
總錢 = 30  # 錢
總酒 = 2  # 斗

# 假設情況 1: 醇酒 5 升，行酒 1 斗 5 升，盈餘 10 錢
盈 = 10  # 錢
醇酒率_1 = 5  # 升
行酒率_1 = 15  # 升 (1 斗 5 升)

# 假設情況 2: 醇酒 2 升，行酒 1 斗 8 升，不足 2 錢
不足 = 2  # 錢
醇酒率_2 = 2  # 升
行酒率_2 = 18  # 升 (1 斗 8 升)

# 盈不足術計算
# 令維乘所出率，并以為實
實 = (醇酒率_1 * 不足 + 醇酒率_2 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
醇酒量 = Fraction(實, 法)  # 醇酒量 (升)

# 行酒量
行酒量 = 總酒 * 10 - 醇酒量  # 總酒量轉為升後減去醇酒量

# 將醇酒量轉為升，行酒量轉為斗
a = 醇酒量  # 醇酒量 (升)
b = Fraction(行酒量, 10)  # 行酒量 (斗)
"""
"""
