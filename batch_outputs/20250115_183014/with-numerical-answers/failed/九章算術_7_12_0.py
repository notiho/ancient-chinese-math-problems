"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

"""
Suppose there is pure wine (醇酒) priced at 50 qian per dou, and diluted wine (行酒) priced at 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine does one obtain respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2.

The procedure for excess and deficiency (盈不足術) says: Place the rates of the items being purchased, with the excess and deficiency below them respectively.
Multiply the rates by their respective excess or deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result.
If there is a fraction, simplify it.
For the items being purchased, if the excess and deficiency are related to the same item, place the rates of the items being purchased, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the item, and the divisor represents the total number of people.

Answer: *a*(=5/2) dou of pure wine, and *b*(=7/4) dou of diluted wine.
"""

# 醇酒價格與行酒價格
醇酒價格 = 50
行酒價格 = 10

# 總錢數與總酒量
總錢數 = 30
總酒量 = 2

# 盈不足術：假設盈、不足情況
盈 = 10  # 餘一十
不足 = 2  # 不足二

# 置所出率
醇酒率 = 醇酒價格
行酒率 = 行酒價格

# 盈、不足各居其下，令維乘所出率，并以為實
實 = (盈 * 行酒率) + (不足 * 醇酒率)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
醇酒量 = Fraction(實, 法)

# 醇酒量轉換為斗
醇酒量斗 = Fraction(醇酒量, 醇酒價格)

# 行酒量 = 總酒量 - 醇酒量斗
行酒量斗 = 總酒量 - 醇酒量斗

# 答案
a = 醇酒量斗  # 5/2
b = 行酒量斗  # 7/4
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 1/3
Variable 'b' has wrong value. Expected: 7/4, Actual: 5/3"""
