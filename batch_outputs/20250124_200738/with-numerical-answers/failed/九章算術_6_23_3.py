"""
今有假田，初假之歲三畝一錢，明年四畝一錢，後年五畝一錢。凡三歲得一百，問︰田幾何？
術曰：置畝數及錢數，令畝數互乘錢數，并以為法。畝數相乘，又以百錢乘之，為實。實如法得一畝。
荅曰： a(=60/47)頃 。
"""

#----- content starts here -----
"""
Suppose there is rented land. In the first year, 3 mu cost 1 qian. In the second year, 4 mu cost 1 qian. In the third year, 5 mu cost 1 qian.
In total, over three years, 100 qian is earned.
Question: how much land is there?

The procedure says: Place the mu numbers and qian numbers. Let the mu numbers cross-multiply the qian numbers and sum them to form the divisor.
Cross-multiply the mu numbers again, and also multiply them by 100 qian to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

Answer: *a*(=60/47) qing.
"""

from fractions import Fraction

# 初假之歲三畝一錢，明年四畝一錢，後年五畝一錢
畝數 = [3, 4, 5]
錢數 = [1, 1, 1]

# 置畝數及錢數，令畝數互乘錢數，并以為法
法 = sum(畝數[i] * 錢數[i] for i in range(len(畝數)))

# 畝數相乘
畝積 = 1
for 畝 in 畝數:
    畝積 *= 畝

# 又以百錢乘之，為實
百錢 = 100
實 = 畝積 * 百錢

# 實如法得一畝
畝數總 = Fraction(實, 法)

# Convert to qing (100 mu = 1 qing)
a = 畝數總 / 100  # 60/47 qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5"""
