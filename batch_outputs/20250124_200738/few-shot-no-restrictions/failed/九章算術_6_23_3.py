"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, 3 mu is rented for 1 qian. 
In the second year, 4 mu is rented for 1 qian. 
In the third year, 5 mu is rented for 1 qian. 
In total, over three years, 100 qian is paid.
Question: how much land is rented?

The procedure says: Place the mu numbers and qian numbers. 
Let the mu numbers multiply the qian numbers alternately and sum them to form the divisor.
Let the mu numbers multiply each other, and also multiply by 100 qian, to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

Answer: *a* qing.
"""

from fractions import Fraction

# Initial data
畝數 = [3, 4, 5]  # Mu rented in each year
錢數 = [1, 1, 1]  # Qian paid in each year
總錢數 = 100  # Total qian paid over three years

# Calculate the divisor (法)
法 = sum(畝數[i] * 錢數[j] for i in range(len(畝數)) for j in range(len(錢數)))

# Calculate the dividend (實)
實 = 1
for mu in 畝數:
    實 *= mu
實 *= 總錢數

# Calculate the result in mu
畝 = Fraction(實, 法)

# Convert mu to qing (1 qing = 100 mu)
a = Fraction(畝, 100)

a  # Answer in qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5/3"""
