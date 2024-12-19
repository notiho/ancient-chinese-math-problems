#今有三分之一五分之二問合之得幾何
#合分術曰母互乘子并以爲實母相乘爲法實如法而一不滿法者以法命之其母同者直相從之
#荅曰 a(15) 分之 b(11)
# 三分之一五分之二
分子1 = 1
分母1 = 3
分子2 = 2
分母2 = 5

# 母互乘
母互乘 = 分母1 * 分母2

# 子并以爲實
實 = 分子1 * 分母2 + 分子2 * 分母1

# 母相乘爲法
法 = 母互乘

# 實如法而一
a = 實
b = 法

# 不滿法者以法命之
# Already handled by the fraction representation

# 答案
a = Fraction(a, b).numerator
b = Fraction(a, b).denominator