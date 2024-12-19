#今有田廣七分步之四從五分步之三問爲田幾何
#乘分術曰母相乘爲法子相乘爲實實如法而一
#荅曰 a(12/35)步
# 廣七分步之四
廣 = Fraction(4, 7)

# 從五分步之三
從 = Fraction(3, 5)

# 母相乘爲法
法 = 廣.denominator * 從.denominator

# 子相乘爲實
實 = 廣.numerator * 從.numerator

# 實如法而一
a = Fraction(實, 法)