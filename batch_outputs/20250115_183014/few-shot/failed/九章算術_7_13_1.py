"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel hold 3 hu. 
One large vessel and five small vessels hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou. 
Adjust it so that the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the given rates, with surplus and deficit below each. 
Multiply the rates by their respective surplus or deficit, and sum them to get the dividend. 
Sum the surplus and deficit to get the divisor. 
Divide the dividend by the divisor to get the result. If there is a fraction, simplify it. 
For surplus and deficit problems where the same goods are involved, subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

# 大器五、小器一容三斛
rate1_large = 5
rate1_small = 1
total1 = 3  # in hu

# 大器一、小器五容二斛
rate2_large = 1
rate2_small = 5
total2 = 2  # in hu

# 盈不足術
# 盈、不足各居其下
盈 = total1
不足 = total2

# 令維乘所出率，并以為實
實 = (rate1_large * total2) + (rate2_large * total1)

# 并盈、不足為法
法 = (rate1_large + rate2_large)

# 實如法而一
a = Fraction(实
"""
Code error: '(' was never closed (<string>, line 42)"""
