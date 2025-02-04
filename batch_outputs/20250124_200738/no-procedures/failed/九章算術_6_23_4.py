"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, the rent is 3 mu per qian. In the second year, the rent is 4 mu per qian. In the third year, the rent is 5 mu per qian. Over three years, the total rent collected is 100 qian.
Question: how large is the land?

Answer: the land is *a* qing.
"""

# Rent rates for each year (in mu per qian)
rent_rate_year1 = 3
rent_rate_year2 = 4
rent_rate_year3 = 5

# Total rent collected over 3 years (in qian)
total_rent = 100

# Total land rented is the sum of land rented each year
# Land rented each year = rent rate * rent collected for that year
# Since the rent collected is the same each year, divide total rent by 3 to get yearly rent
yearly_rent = Fraction(total_rent, 3)

# Calculate total land rented
total_land = (rent_rate_year1 * yearly_rent) + (rent_rate_year2 * yearly_rent) + (rent_rate_year3 * yearly_rent)

# Convert total land from mu to qing (1 qing = 100 mu)
a = Fraction(total_land, 100)  # Total land in qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 4"""
