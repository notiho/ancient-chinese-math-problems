#又有二分之一三分之二四分之三五分之四問合之得幾何
#合分術曰母互乘子并以爲實母相乘爲法實如法而一不滿法者以法命之其母同者直相從之
#荅曰得 a(60) 分之 b(163)
# 分數列表
分數列表 = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(4, 5)]

# 母互乘
母相乘 = 1
for 分數 in 分數列表:
    母相乘 *= 分數.denominator

# 子并以爲實
子相加 = 0
for 分數 in 分數列表:
    子相加 += 分數.numerator * (母相乘 // 分數.denominator)

# 實如法而一
實 = 子相加
法 = 母相乘

# 不滿法者以法命之
a = 法
b = 實

# 答案
結果 = Fraction(b, a)  # 簡化分數
a = 結果.denominator
b = 結果.numerator