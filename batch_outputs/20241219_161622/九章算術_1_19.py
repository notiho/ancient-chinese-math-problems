#又有田廣九分步之七從十一分步之九問爲田幾何
#乘分術曰母相乘爲法子相乘爲實實如法而一
#荅曰 a(7/11)步
# 廣九分步之七
廣 = Fraction(7, 9)

# 從十一分步之九
從 = Fraction(9, 11)

# 母相乘爲法
法 = 廣.denominator * 從.denominator

# 子相乘爲實
實 = 廣.numerator * 從.numerator

# 實如法而一
a = Fraction(實, 法)