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

The procedure says: Place the mu numbers and qian numbers. Let the mu numbers multiply each other with the qian numbers, and sum them to form the divisor.
Let the mu numbers multiply each other, and then multiply by 100 qian to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

The answer says: *a* qing.
"""

from fractions import Fraction

# 初假之歲三畝一錢
畝數_1 = 3
錢數_1 = 1

# 明年四畝一錢
畝數_2 = 4
錢數_2 = 1

# 後年五畝一錢
畝數_3 = 5
錢數_3 = 1

# 凡三歲得一百
總錢數 = 100

# 令畝數互乘錢數，并以為法
法 = (畝數_1 * 錢數_1) + (畝數_2 * 錢數_2) + (畝數_3 * 錢數_3)

# 畝數相乘，又以百錢乘之，為實
實 = 畝數_1 * 畝數_2 * 畝數_3 * 總錢數

# 實如法得一畝
畝數 = Fraction(實, 法)

# 1頃 = 100畝
a = Fraction(畝數, 100)  # Convert to qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 5"""
