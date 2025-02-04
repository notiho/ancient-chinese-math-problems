"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, 3 mu cost 1 qian; in the second year, 4 mu cost 1 qian; in the third year, 5 mu cost 1 qian.
In total, over three years, 100 qian is paid.
Question: how much land is there?

The procedure says: Place the mu values and qian values. Let the mu values multiply each other's qian values, and sum them to form the divisor.
Let the mu values multiply each other, and also multiply by 100 qian, forming the dividend.
Divide the dividend by the divisor to obtain the number of mu.

The answer says: *a* qing.
"""

from fractions import Fraction

# Initial data
畝數 = [3, 4, 5]  # mu values for each year
錢數 = [1, 1, 1]  # qian values for each year
總錢 = 100  # total qian paid over three years

# Calculate the divisor (法)
法 = sum(畝數[i] * 錢數[j] for i in range(len(畝數)) for j in range(len(錢數)) if i != j)

# Calculate the dividend (實)
實 = 畝數[0] * 畝數[1] * 畝數[2] * 總錢

# Calculate the total land in mu
總畝 = Fraction(實, 法)

# Convert mu to qing (1 qing = 100 mu)
a = Fraction(總畝, 100)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5/2"""
