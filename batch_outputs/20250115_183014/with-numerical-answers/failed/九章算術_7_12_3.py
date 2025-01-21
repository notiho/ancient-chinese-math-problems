"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：醇酒 a(=5/2)升 ，行酒 b(=7/4)斗 。
"""

"""
Suppose there is pure wine (醇酒) priced at 50 qian per dou, and diluted wine (行酒) priced at 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, leaving a deficit of 2.
The procedure for surplus and deficit says: Place the rates of output, with the surplus and deficit below each.
Multiply the rates of output by their respective surplus or deficit, and add them to obtain the dividend.
Add the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
If the surplus and deficit correspond to the same item being purchased, place the rates of output, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a*(=5/2) sheng of pure wine, and *b*(=7/4) dou of diluted wine.
"""

# 醇酒每斗直錢五十
醇酒率 = 50

# 行酒每斗直錢一十
行酒率 = 10

# 錢三十，得酒二斗
總錢 = 30
總酒 = 2  # in dou

# 盈不足術
# 假令醇酒五升，行酒一斗五升，有餘一十
盈_醇酒 = Fraction(5, 10)  # 5 sheng = 0.5 dou
盈_行酒 = 1 + Fraction(5, 10)  # 1.5 dou
盈 = 10

# 令之醇酒二升，行酒一斗八升，不足二
不足_醇酒 = Fraction(2, 10)  # 2 sheng = 0.2 dou
不足_行酒 = 1 + Fraction(8, 10)  # 1.8 dou
不足 = -2

# 置所出率，盈、不足各居其下
盈實 = 醇酒率 * 盈 + 行酒率 * 盈
不足實 = 醇酒率 * 不足 + 行酒率 * 不足

# 令維乘所出率，并以為實
實 = 醇酒率 * abs(盈) + 行酒率 * abs(不足)

# 并盈、不足為法
法 = abs(盈) + abs(不足)

# 實如法而一
醇酒量 = Fraction(實, 法)

# 醇酒量 = 5/2 dou

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
