#又有田廣五分步之四從九分步之五問爲田幾何
#乘分術曰母相乘爲法子相乘爲實實如法而一
#荅曰 a(4/9)步
# 廣五分步之四
廣 = Fraction(4, 5)

# 從九分步之五
從 = Fraction(5, 9)

# 母相乘爲法
法 = 廣.denominator * 從.denominator

# 子相乘爲實
實 = 廣.numerator * 從.numerator

# 實如法而一
a = Fraction(實, 法)