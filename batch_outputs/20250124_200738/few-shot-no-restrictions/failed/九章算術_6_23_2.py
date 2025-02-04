"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, the rent is 3 mu per qian. In the second year, the rent is 4 mu per qian. In the third year, the rent is 5 mu per qian.
Over the course of three years, the total rent collected is 100 qian.
Question: how much land is rented?

The procedure says: Place the mu values and qian values. Let the mu values multiply each other's qian values, and sum them to form the divisor.
Let the mu values multiply each other, and also multiply by 100 qian to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

Answer: *a* qing.
"""

from fractions import Fraction

# Initial data
mu_values = [3, 4, 5]  # mu per qian for each year
qian_values = [1, 1, 1]  # qian per year
total_qian = 100  # total rent collected over 3 years

# Step 1: Calculate the divisor (法)
法 = sum(mu_values[i] * qian_values[i] for i in range(len(mu_values)))

# Step 2: Calculate the dividend (實)
實 = 1
for mu in mu_values:
    實 *= mu
實 *= total_qian

# Step 3: Calculate the total land in mu
total_mu = Fraction(實, 法)

# Step 4: Convert mu to qing (100 mu = 1 qing)
a = Fraction(total_mu, 100)

# Output the result
a  # Total land in qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5"""
