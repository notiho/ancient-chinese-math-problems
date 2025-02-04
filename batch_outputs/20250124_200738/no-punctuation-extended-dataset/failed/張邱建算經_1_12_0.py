"""
今有圓材徑頭二尺一寸欲以為方問各㡬何
術曰置徑尺寸數以五乗之為實以七為法實如法而一
答曰 a尺
"""

#----- content starts here -----
"""
Suppose there is a cylindrical log with a diameter of 2 chi and 1 cun. It is desired to square it into a square cross-section.
Question: what is the side length of the square cross-section?

The procedure says: Place the diameter in chi and cun. Multiply it by itself five times (raise it to the power of 2.5), obtaining the dividend.
Take 7 as the divisor.
Divide the dividend by the divisor, obtaining the side length.

Answer: *a* chi.
"""

from fractions import Fraction

# 圓材徑頭二尺一寸
徑 = 2 + Fraction(1, 10)  # 2 chi and 1 cun (1 cun = 1/10 chi)

# 置徑尺寸數，以五乗之為實
實 = 徑 ** Fraction(5, 2)  # Raising to the power of 2.5

# 以七為法
法 = 7

# 實如法而一
a = Fraction(實, 法)  # Side length of the square cross-section in chi#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
