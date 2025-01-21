"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there is a large vessel and a small vessel. Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou. 
Adjust the values such that the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, leaving a deficit of 2 dou.

The "excess and deficit" procedure says: Place the coefficients of the large and small vessels (the rates) under their respective totals of excess and deficit. 
Multiply the coefficients by their respective totals and sum them to form the dividend. 
Sum the excess and deficit to form the divisor. 
Divide the dividend by the divisor to find the value of one unit. 
If there is a remainder, adjust it proportionally. 
The excess and deficit are then used to determine the values of the large and small vessels.

Answer: The large vessel holds *a* hu, and the small vessel holds *b* hu.
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
# Multiply the rates by their respective totals
numerator = (rate1_large * total2) + (rate2_large * total1)

# 并盈不足为法
denominator = (rate1_large + rate2_large)

# 实如法而一
unit_value = Fraction(numerator, denominator)

# 大器容
a = Fraction(rate1_large * unit_value, rate1_large + rate1_small)

# 小器容
b = Fraction(rate2_small * unit_value, rate2_large + rate2_small)
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 65/36
Variable 'b' has wrong value. Expected: 7/24, Actual: 65/36"""
