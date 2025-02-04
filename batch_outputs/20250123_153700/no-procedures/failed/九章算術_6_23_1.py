"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
荅曰： a頃 。
"""

"""
Suppose there is rented land. In the first year, the rent is 3 mu per qian, in the second year, 4 mu per qian, and in the third year, 5 mu per qian. Over the course of three years, the total rent collected is 100 qian.
Question: how large is the land?

Answer: the land is *a* qing.
"""

# Rent rates per year (mu per qian)
rate_year_1 = Fraction(3, 1)  # 3 mu per qian
rate_year_2 = Fraction(4, 1)  # 4 mu per qian
rate_year_3 = Fraction(5, 1)  # 5 mu per qian

# Total rent collected over 3 years (in qian)
total_rent = 100

# Total land rented (in mu) is the weighted average of the rates over 3 years
total_land_mu = total_rent * (rate_year_1 + rate_year_2 + rate_year_3)

# Convert mu to qing (1 qing = 100 mu)
a = Fraction(total_land_mu, 100)  # Convert mu to qing

a  # The size of the land in qing
"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 12"""
