"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, 3 mu cost 1 qian. In the second year, 4 mu cost 1 qian. In the third year, 5 mu cost 1 qian.
Over three years, the total rent collected is 100 qian.
Question: how much land is there?

The procedure says: Place the mu numbers and qian numbers. Let the mu numbers multiply each other, and let the qian numbers multiply each other. Add these together to form the divisor.
Let the mu numbers multiply each other again, and also multiply by 100 qian. This forms the dividend.
Divide the dividend by the divisor to obtain the number of mu.

Answer: *a* qing.
"""

from fractions import Fraction

# 初假之歲三畝一錢，明年四畝一錢，後年五畝一錢
畝數 = [3, 4, 5]
錢數 = [1, 1, 1]

# 置畝數及錢數，令畝數互乘錢數，并以為法
法 = sum(畝數[i] * 畝數[j] * 錢數[i] * 錢數[j] for i in range(len(畝數)) for j in range(len(畝數)))

# 畝數相乘，又以百錢乘之，為實
實 = 100 * sum(畝數[i] * 畝數[j] for i in range(len(畝數)) for j in range(len(畝數)))

# 實如法得一畝
畝數總 = Fraction(實, 法)

# 1頃 = 100畝
a = Fraction(畝數總, 100)  # Convert to qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 1"""
