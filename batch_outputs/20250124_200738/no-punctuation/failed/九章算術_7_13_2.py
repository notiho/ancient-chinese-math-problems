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

The procedure says: Suppose the large vessel holds 5 dou, and the small vessel also holds 5 dou, making a total of 10 dou.
Adjust this by letting the large vessel hold 5 dou and 5 sheng, and the small vessel hold 2 dou and 5 sheng, resulting in a shortfall of 2 dou.

The procedure for surplus and shortfall says: Place the rates of output (the coefficients of the vessels) under the surplus and shortfall, respectively.
Multiply the rates of output by their corresponding surplus or shortfall, and sum these to form the dividend.
Sum the surplus and shortfall to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For surplus and shortfall problems involving buying goods, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend accordingly.

Answer: the large vessel holds *a* hu, and the small vessel holds *b* hu.
"""

# Given data:
# Five large vessels and one small vessel hold 3 hu
# One large vessel and five small vessels hold 2 hu

# Coefficients for the vessels
large_vessel_coeff_1 = 5  # Coefficient for large vessels in the first equation
small_vessel_coeff_1 = 1  # Coefficient for small vessels in the first equation
total_1 = 3  # Total hu in the first equation

large_vessel_coeff_2 = 1  # Coefficient for large vessels in the second equation
small_vessel_coeff_2 = 5  # Coefficient for small vessels in the second equation
total_2 = 2  # Total hu in the second equation

# Surplus and shortfall method:
# Calculate the surplus and shortfall
surplus = large_vessel_coeff_1 * total_2 - large_vessel_coeff_2 * total_1
shortfall = small_vessel_coeff_2 * total_1 - small_vessel_coeff_1 * total_2

# Sum the surplus and shortfall to form the divisor
divisor = surplus + shortfall

# Multiply the rates of output by their corresponding surplus or shortfall to form the dividend
dividend_large = total_2 * small_vessel_coeff_1 - total_1 * small_vessel_coeff_2
dividend_small = total_1 * large_vessel_coeff_2 - total_2 * large_vessel_coeff_1

# Divide the dividend by the divisor to find the result
a = Fraction(dividend_large, divisor)  # Large vessel capacity in hu
b = Fraction(dividend_small, divisor)  # Small vessel capacity in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13/24, Actual: -13/20
Variable 'b' has wrong value. Expected: 7/24, Actual: -7/20"""
