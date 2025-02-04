"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
Suppose there are five large vessels and one small vessel that together hold 3 hu.
Also, one large vessel and five small vessels together hold 2 hu.
Question: how much does each large and small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou.
Suppose the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, resulting in a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients (rates) of the vessels, with the surplus and deficit below each.
Multiply the coefficients by the surplus or deficit, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to find the value of one vessel.
If there is a fraction, simplify it.
For the surplus and deficit to match the purchase of the same item, place the coefficients, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend represents the value of the item, and the divisor represents the number of people.

Answer: The large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# 大器五、小器一容三斛
大器率1 = 5
小器率1 = 1
總量1 = 3  # 3 hu

# 大器一、小器五容二斛
大器率2 = 1
小器率2 = 5
總量2 = 2  # 2 hu

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 總量1
不足 = 總量2

# 令維乘所出率，并以為實
實 = (大器率1 * 不足) + (大器率2 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
大器 = Fraction(實, 法)

# 小器容 = 總量1 - (大器率1 * 大器) / 小器率1
小器 = Fraction(總量1 - (大器率1 * 大器), 小器率1)

# 答案
a = 大器
b = 小器
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 13/5
Variable 'b' has wrong value. Expected: 7/24, Actual: -10"""
