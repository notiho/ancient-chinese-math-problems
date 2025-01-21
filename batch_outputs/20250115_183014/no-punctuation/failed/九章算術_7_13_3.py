"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel together hold 3 hu.
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose each large vessel holds 5 dou, and each small vessel also holds 5 dou, making a total of 10 dou.
Adjust it such that each large vessel holds 5 dou and 5 sheng, and each small vessel holds 2 dou and 5 sheng, leaving a shortage of 2 dou.

The procedure for surplus and shortage says: Place the coefficients of the given rates of surplus and shortage below each other.
Multiply the coefficients of the given rates, and sum them to form the dividend.
Sum the surplus and shortage to form the divisor.
Divide the dividend by the divisor, and if there is a remainder, simplify it.
The surplus and shortage are then adjusted proportionally.
For the final answer, place the coefficients of the given rates, subtract the smaller from the larger, and reduce the divisor and dividend proportionally.

Answer: Each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

# 大器五小器一容三斛
rate1_large = 5
rate1_small = 1
total1 = 3  # in hu

# 大器一小器五容二斛
rate2_large = 1
rate2_small = 5
total2 = 2  # in hu

# 盈不足術
# 置所出率盈不足各居其下
盈 = rate1_large * total2 - rate2_large * total1  # Surplus
不足 = rate2_small * total1 - rate1_small * total2  # Shortage

# 并以為實
實 = rate1_large * rate2_small - rate2_large * rate1_small

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
unit = Fraction(實, 法)

# 大器容
a = unit * rate2_small

# 小器容
b = unit * rate1_large
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 6
Variable 'b' has wrong value. Expected: 7/24, Actual: 6"""
