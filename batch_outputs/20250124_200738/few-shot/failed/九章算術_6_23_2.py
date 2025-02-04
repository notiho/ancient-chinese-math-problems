"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, 3 mu cost 1 qian. In the second year, 4 mu cost 1 qian. In the third year, 5 mu cost 1 qian.
In total, 100 qian is paid over three years.
Question: how much land is there?

The procedure says: Place the mu numbers and qian numbers. Let the mu numbers multiply each other, and the qian numbers multiply each other, then sum them to form the divisor.
Let the mu numbers multiply each other again, and also multiply by 100 qian, forming the dividend.
Divide the dividend by the divisor to obtain the number of mu.

Answer: *a* qing.
"""

from fractions import Fraction

# 初假之歲三畝一錢，明年四畝一錢，後年五畝一錢
畝數 = [3, 4, 5]
錢數 = [1, 1, 1]

# 令畝數互乘錢數，并以為法
法 = sum(畝數[i] * 錢數[i] for i in range(3))

# 畝數相乘
畝積 = 畝數[0] * 畝數[1] * 畝數[2]

# 又以百錢乘之，為實
百錢 = 100
實 = 畝積 * 百錢

# 實如法得一畝
畝數總 = Fraction(實, 法)

# 100 畝為 1 頃
a = Fraction(畝數總, 100)  # Convert mu to qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5"""
