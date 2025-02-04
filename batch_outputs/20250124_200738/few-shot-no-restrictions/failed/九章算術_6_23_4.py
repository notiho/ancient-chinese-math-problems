"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, 3 mu cost 1 qian; in the second year, 4 mu cost 1 qian; in the third year, 5 mu cost 1 qian.
In total, over three years, 100 qian were paid.
Question: how much land was rented?

The procedure says: Place the mu values and qian values. Let the mu values multiply each other's qian values, and sum them to form the divisor.
Let the mu values multiply each other, and also multiply by 100 qian, to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

The answer says: *a* qing.
"""

from fractions import Fraction

# Data for each year
畝數 = [3, 4, 5]  # mu values
錢數 = [1, 1, 1]  # qian values
總錢 = 100  # total qian paid over three years

# Step 1: 畝數互乘錢數，并以為法
法 = sum(畝數[i] * 錢數[i] for i in range(len(畝數)))

# Step 2: 畝數相乘，又以百錢乘之，為實
實 = 1
for 畝 in 畝數:
    實 *= 畝
實 *= 總錢

# Step 3: 實如法得一畝
一畝 = Fraction(實, 法)

# Convert mu to qing (1 qing = 100 mu)
a = Fraction(一畝, 100)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5"""
