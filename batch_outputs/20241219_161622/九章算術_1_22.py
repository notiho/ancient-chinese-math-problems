#又有田廣七步四分步之三從十五步九分步之五問爲田幾何
#大廣田術曰分母各乘其全分子從之相乘爲實分母相乘爲法實如法而一
#荅曰 a(1085/9)步

from fractions import Fraction

# 廣七步四分步之三
廣 = 7 + Fraction(3, 4)

# 從十五步九分步之五
從 = 15 + Fraction(5, 9)

# 分母各乘其全，分子從之相乘爲實
實 = 廣 * 從

# 分母相乘爲法
法 = 1  # In this case, the fractions are already combined in `實`

# 實如法而一
a = 實
