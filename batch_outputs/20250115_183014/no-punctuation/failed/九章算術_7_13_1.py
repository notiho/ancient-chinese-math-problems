"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there are large vessels and small vessels. Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu.
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose each large vessel holds 5 dou and each small vessel also holds 5 dou, making a total of 10 dou.
Adjust the values such that a large vessel holds 5 dou and 5 sheng, and a small vessel holds 2 dou and 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients of the surplus and deficit under their respective terms.
Multiply the coefficients by their respective terms and sum them to form the dividend.
Sum the surplus and deficit coefficients to form the divisor.
Divide the dividend by the divisor. If there is a remainder, convert it into a fraction.
The surplus and deficit are then balanced.

For goods purchased with surplus and deficit, place the coefficients of the surplus and deficit, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the value of the goods, and the divisor represents the number of people.

Answer: Each large vessel holds *a* hu, and each small vessel holds *b* hu.
"""

# Large vessel and small vessel coefficients
大器率 = 5
小器率 = 1
盈率 = 3  # 3 hu for 5 large + 1 small
不足率 = 2  # 2 hu for 1 large + 5 small

# Surplus and deficit coefficients
盈 = 5  # Coefficient of large vessels in surplus equation
不足 = 1  # Coefficient of small vessels in surplus equation

# Place coefficients and calculate dividend and divisor
實 = (盈 * 不足率) + (不足 * 盈率)  # Dividend
法 = 盈 + 不足  # Divisor

# Divide to find the value of one large vessel
大器 = Fraction(實, 法)

# Use the value of the large vessel to find the value of the small vessel
小器 = Fraction(盈率 - (大器 * 大器率), 小器率)

# Convert to hu
a = 大器
b = 小器
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 13/6
Variable 'b' has wrong value. Expected: 7/24, Actual: -47/6"""
