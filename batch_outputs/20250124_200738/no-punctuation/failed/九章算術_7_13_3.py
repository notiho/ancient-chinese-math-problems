"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰大器容 a斛 小器容 b斛 
"""

#----- content starts here -----
"""
Suppose there is a large vessel and a small vessel. Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou and the small vessel also holds 5 dou, making a total of 10 dou.
Adjust it so that the large vessel holds 5 dou 5 sheng and the small vessel holds 2 dou 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients of the equations (rates of output) under the surplus and deficit values. 
Multiply the coefficients by the surplus and deficit, respectively, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the value of one unit. If there is a fraction, simplify it.
For surplus and deficit problems, if the surplus and deficit are equal, the solution is consistent.
If the surplus and deficit differ, adjust the coefficients to reduce the difference and simplify the divisor and dividend.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

# Coefficients for the equations
# 5 large vessels + 1 small vessel = 3 hu
# 1 large vessel + 5 small vessels = 2 hu
大器率1 = 5
小器率1 = 1
總量1 = 3

大器率2 = 1
小器率2 = 5
總量2 = 2

# Surplus and deficit method
# 盈不足各居其下
盈 = 總量1 * 小器率2 - 總量2 * 小器率1  # Surplus
不足 = 總量2 * 大器率1 - 總量1 * 大器率2  # Deficit

# 所出率
所出率盈 = 大器率1 * 小器率2
所出率不足 = 小器率1 * 大器率2

# 令維乘所出率并以為實
實 = 盈 * 所出率盈 + 不足 * 所出率不足

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
單位值 = Fraction(實, 法)

# 大器容
a = Fraction(總量1 * 小器率2 - 總量2 * 小器率1, 法)

# 小器容
b = Fraction(總量2 * 大器率1 - 總量1 * 大器率2, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 13/20
Variable 'b' has wrong value. Expected: 7/24, Actual: 7/20"""
