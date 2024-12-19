#今有三分之一三分之二四分之三問減多益少各幾何而平
#平分術曰母互乘子副并爲平實母相乘爲法以列數乘未并者各自爲列實亦以列數乘法以平實減列實餘約之爲所減并所減以益於少以法命平實各得其平
#荅曰減 a(4) 分之 b(3) 者 c(2) d(3) 分之 e(2) 者 f(1) 并以益 g(3) 分之 h(1) 而各平於 i(12) 分之 j(7)

from fractions import Fraction

# 列數
數列 = [Fraction(1, 3), Fraction(2, 3), Fraction(3, 4)]

# 母互乘
母互乘 = [數列[1].denominator * 數列[2].denominator, 
          數列[0].denominator * 數列[2].denominator, 
          數列[0].denominator * 數列[1].denominator]

# 子副并爲平實
平實 = sum([數列[i].numerator * 母互乘[i] for i in range(len(數列))])

# 母相乘爲法
法 = 數列[0].denominator * 數列[1].denominator * 數列[2].denominator

# 以列數乘未并者各自爲列實
列實 = [數列[i].numerator * 法 // 數列[i].denominator for i in range(len(數列))]

# 以平實減列實餘約之爲所減
所減 = [Fraction(平實 - 列實[i], 法) for i in range(len(列實))]

# 并所減以益於少
益於少 = sum(所減)

# 以法命平實各得其平
平 = Fraction(平實, 法)

# 結果
a, b, c = 所減[0].numerator, 所減[0].denominator, 所減[0]
d, e, f = 所減[1].numerator, 所減[1].denominator, 所減[1]
g, h = 益於少.numerator, 益於少.denominator
i, j = 平.numerator, 平.denominator
