"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, the rent is 3 mu per qian. In the second year, the rent is 4 mu per qian. In the third year, the rent is 5 mu per qian. Over the course of three years, the total rent collected is 100 qian.
Question: how large is the land?

Answer: *a* qing.
"""

# Rent rates per year (in mu per qian)
rate_year_1 = Fraction(3, 1)  # 3 mu per qian
rate_year_2 = Fraction(4, 1)  # 4 mu per qian
rate_year_3 = Fraction(5, 1)  # 5 mu per qian

# Total rent collected over 3 years (in qian)
total_rent = 100

# Total land rented (in mu) is the sum of land rented each year
# Land rented each year is the rent rate multiplied by the rent collected for that year
# Let x be the rent collected each year (in qian)
# x + x + x = total_rent
rent_per_year = Fraction(total_rent, 3)

# Total land rented (in mu)
total_land_mu = rent_per_year * rate_year_1 + rent_per_year * rate_year_2 + rent_per_year * rate_year_3

# Convert total land from mu to qing (1 qing = 100 mu)
a = Fraction(total_land_mu, 100)  # Convert mu to qing

a  # The total land in qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 4"""
