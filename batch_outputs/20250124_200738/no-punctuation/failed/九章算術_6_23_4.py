"""
今有假田初假之歲三畝一錢明年四畝一錢後年五畝一錢凡三歲得一百問田幾何
術曰置畝數及錢數令畝數互乘錢數并以為法畝數相乘又以百錢乘之為實實如法得一畝
荅曰 a頃 
"""

#----- content starts here -----
"""
Suppose there is a rented field. In the first year, 3 mu cost 1 qian. In the second year, 4 mu cost 1 qian. In the third year, 5 mu cost 1 qian.
In total, over 3 years, 100 qian is paid.
Question: how large is the field?

The procedure says: Place the mu numbers and the qian numbers.
Let the mu numbers multiply each other, and sum the qian numbers to form the divisor.
Let the mu numbers multiply each other again, and also multiply by 100 qian to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

The answer says: *a* qing.
"""

from fractions import Fraction

# 初假之歲三畝一錢
畝數1 = 3
錢數1 = 1

# 明年四畝一錢
畝數2 = 4
錢數2 = 1

# 後年五畝一錢
畝數3 = 5
錢數3 = 1

# 凡三歲得一百
總錢數 = 100

# 畝數互乘
畝積 = 畝數1 * 畝數2 * 畝數3

# 錢數并以為法
法 = 錢數1 + 錢數2 + 錢數3

# 畝數相乘又以百錢乘之為實
實 = 畝積 * 總錢數

# 實如法得一畝
畝數 = Fraction(實, 法)

# 100 畝為 1 頃
a = Fraction(畝數, 100)  # Convert to qing#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/47, Actual: 20"""
