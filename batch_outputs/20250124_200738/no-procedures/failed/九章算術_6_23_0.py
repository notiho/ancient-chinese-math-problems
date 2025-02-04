"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, the rent is 3 mu per qian. In the second year, the rent is 4 mu per qian. In the third year, the rent is 5 mu per qian. Over three years, the total rent collected is 100 qian.
Question: how much land is there?

Answer: the land is *a* qing.
"""

# Rent rates for each year (mu per qian)
rate_year_1 = Fraction(3, 1)  # 3 mu per qian
rate_year_2 = Fraction(4, 1)  # 4 mu per qian
rate_year_3 = Fraction(5, 1)  # 5 mu per qian

# Total rent collected over 3 years (in qian)
total_rent = 100

# Total land rented (in mu) is the weighted average of the rent rates over 3 years
total_land = total_rent * (rate_year_1 + rate_year_2 + rate_year_3)

# Convert total land from mu to qing (1 qing = 100 mu)
a = Fraction(total_land, 100)  # Convert mu to qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 12"""
