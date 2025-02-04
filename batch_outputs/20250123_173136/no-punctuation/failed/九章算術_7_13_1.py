"""
今有大器五小器一容三斛大器一小器五容二斛問大小器各容幾何
術曰假令大器五斗小器亦五斗盈一十斗令之大器五斗五升小器二斗五升不足二斗
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰大器容 a斛 小器容 b斛 
"""

"""
Suppose there are large and small vessels. Five large vessels and one small vessel together hold 3 hu. 
One large vessel and five small vessels together hold 2 hu. 
Question: how much does each large vessel and each small vessel hold?

The procedure says: Suppose each large vessel holds 5 dou and each small vessel also holds 5 dou, making a total of 10 dou.
Adjust the values such that the large vessel holds 5 dou and 5 sheng, and the small vessel holds 2 dou and 5 sheng, leaving a deficit of 2 dou.

The procedure for surplus and deficit says: Place the coefficients of the surplus and deficit below their respective equations.
Multiply the coefficients by their respective surplus or deficit, summing them to form the dividend.
Sum the coefficients to form the divisor.
Divide the dividend by the divisor to find the value of one unit. If there is a remainder, convert it into fractional form.
The surplus and deficit are then adjusted proportionally.

Answer: The large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

from fractions import Fraction

# Coefficients for the equations
大器率1 = 5  # Coefficient of large vessels in the first equation
小器率1 = 1  # Coefficient of small vessels in the first equation
總量1 = 3    # Total volume in the first equation (in hu)

大器率2 = 1  # Coefficient of large vessels in the second equation
小器率2 = 5  # Coefficient of small vessels in the second equation
總量2 = 2    # Total volume in the second equation (in hu)

# Step 1: Surplus and deficit method
# Multiply coefficients by their respective totals
實1 = 大器率1 * 總量2  # First equation's coefficient multiplied by the second equation's total
實2 = 大器率2 * 總量1  # Second equation's coefficient multiplied by the first equation's total

# Calculate the surplus and deficit
盈 = 實1 - 小器率1 * 總量2  # Surplus
不足 = 小器率2 * 總量1 - 實2  # Deficit

# Sum the coefficients to form the divisor
法 = 大器率1 * 小器率2 - 大器率2 * 小器率1

# Calculate the value of one unit (volume of one large vessel)
a = Fraction(盈, 法)

# Calculate the value of one small vessel
b = Fraction(不足, 法)
"""
Variable 'a' has wrong value. Expected: 13/24, Actual: 1/3
Variable 'b' has wrong value. Expected: 7/24, Actual: 1/2"""
