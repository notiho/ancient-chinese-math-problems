#今有田廣三步三分步之一從五步五分步之二問爲田幾何
#大廣田術曰分母各乘其全分子從之相乘爲實分母相乘爲法實如法而一
#荅曰 a(18)步

from fractions import Fraction

# 廣三步三分步之一
廣 = 3 + Fraction(1, 3)

# 從五步五分步之二
從 = 5 + Fraction(2, 5)

# 分母各乘其全分子從之相乘爲實
實 = 廣 * 從

# 分母相乘爲法
法 = 1  # Since we are working with fractions, the denominator is already handled.

# 實如法而一
a = 實
