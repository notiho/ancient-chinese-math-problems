#又有二分之一三分之二四分之三問減多益少各幾何而平
#平分術曰母互乘子副并爲平實母相乘爲法以列數乘未并者各自爲列實亦以列數乘法以平實減列實餘約之爲所減并所減以益於少以法命平實各得其平
#荅曰減 a(3) 分之 b(2) 者 c(1) d(4) 分之 e(3) 者 f(4) 并以益 g(2) 分之 h(1) 而各平於 i(36) 分之 j(22)

from fractions import Fraction

# 列出分數
分數 = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]

# 母互乘子副并爲平實
平實 = sum([分數[i].numerator * 分數[j].denominator for i in range(len(分數)) for j in range(len(分數)) if i != j])

# 母相乘爲法
法 = 1
for f in 分數:
    法 *= f.denominator

# 以列數乘未并者各自爲列實
列實 = [f.numerator * 法 // f.denominator for f in 分數]

# 亦以列數乘法以平實減列實餘約之爲所減
所減 = [Fraction(平實 - 列實[i], 法) for i in range(len(列實))]

# 并所減以益於少
益於少 = sum(所減)

# 以法命平實各得其平
各平 = Fraction(平實, 法)

# 結果
a, b = 所減[0].numerator, 所減[0].denominator
c, d = 所減[1].numerator, 所減[1].denominator
e, f = 所減[2].numerator, 所減[2].denominator
g, h = 益於少.numerator, 益於少.denominator
i, j = 各平.numerator, 各平.denominator
