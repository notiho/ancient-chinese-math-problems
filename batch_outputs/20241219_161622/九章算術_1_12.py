#又有九分之八七分之六問孰多多幾何
#課分術曰母互乘子以少減多餘爲實母相乗爲法實如法而一卽相多也
#荅曰 a(9) 分之 b(8) 多多 c(63) 分之 d(2)

from fractions import Fraction

# 九分之八
分數1 = Fraction(8, 9)

# 七分之六
分數2 = Fraction(6, 7)

# 課分術曰母互乘子
實 = 分數1.numerator * 分數2.denominator - 分數2.numerator * 分數1.denominator

# 母相乘爲法
法 = 分數1.denominator * 分數2.denominator

# 實如法而一卽相多也
if 實 > 0:
    a = 法
    b = abs(實)
    c = abs(實)
    d = 法
else:
    a = 法
    b = abs(實)
    c = abs(實)
    d = 法

# Output: a 分之 b 多多 c 分之 d
