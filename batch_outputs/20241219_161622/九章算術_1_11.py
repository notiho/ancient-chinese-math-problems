#今有八分之五二十五分之十六問孰多多幾何
#課分術曰母互乘子以少減多餘爲實母相乗爲法實如法而一卽相多也
#荅曰 a(25) 分之 b(16) 多多 c(200) 分之 d(3)

from fractions import Fraction

# 八分之五
分數1 = Fraction(5, 8)

# 二十五分之十六
分數2 = Fraction(16, 25)

# 課分術曰母互乘子以少減多
實 = abs(分數1 - 分數2)

# 餘爲實母相乘爲法
法 = 分數1.denominator * 分數2.denominator

# 實如法而一卽相多也
a = 實.denominator
b = 實.numerator

# 判斷誰多
if 分數1 > 分數2:
    c = 分數1.numerator
    d = 分數1.denominator
else:
    c = 分數2.numerator
    d = 分數2.denominator
