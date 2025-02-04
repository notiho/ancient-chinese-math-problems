"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a(=13/24)斛 ，小器容 b(=7/24)斛 。
"""

#----- content starts here -----
"""
Suppose there are 5 large vessels and 1 small vessel that together hold 3 hu.
Also, 1 large vessel and 5 small vessels together hold 2 hu.
Question: how much does each large and small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou.
Then suppose the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, resulting in a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients (the number of vessels) with the surplus and deficit below them.
Multiply the coefficients by the surplus and deficit, then sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain the value of one vessel.
If there is a fraction, simplify it.
For surplus and deficit problems where the same item is being purchased, place the coefficients, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: The large vessel holds *a*(=13/24) hu, and the small vessel holds *b*(=7/24) hu.
"""

from fractions import Fraction

# 大器五、小器一容三斛
大器1 = 5
小器1 = 1
總量1 = 3

# 大器一、小器五容二斛
大器2 = 1
小器2 = 5
總量2 = 2

# 盈不足術
# 置所出率，盈、不足各居其下
盈 = 總量1
不足 = 總量2

# 令維乘所出率，并以為實
實 = (大器1 * 不足) + (大器2 * 盈)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
大器 = Fraction(實, 法)

# 小器
小器 = Fraction(總量1 - 大器 * 大器1, 小器1)

a = 大器  # 13/24
b = 小器  # 7/24#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 13/5
Variable 'b' has wrong value. Expected: 7/24, Actual: -10"""
