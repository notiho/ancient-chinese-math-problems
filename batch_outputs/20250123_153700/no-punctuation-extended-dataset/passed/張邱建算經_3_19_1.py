"""
今有甲持錢二十乙持錢五十丙持錢四十丁持錢三十戊持錢六十凡五人合本治生得利二萬五千六百三十五欲以本錢多少分之問各人得幾何
術曰各列置本持錢數副併為法以利錢乘未併者各自為實實如法得一
答曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢
"""

"""
Suppose there are five people: Jia holds 20 qian, Yi holds 50 qian, Bing holds 40 qian, Ding holds 30 qian, and Wu holds 60 qian.
Together, they pooled their capital to engage in business and earned a profit of 25,635 qian.
Question: How much profit does each person receive, proportional to their initial capital?

The procedure says: List the amounts of capital each person contributed.
Add them together to form the divisor.
Multiply the total profit by each individual’s capital (not yet summed) to form the dividend for each person.
Divide the dividend by the divisor to obtain each person’s share.

Answer: Jia gets *a* qian, Yi gets *b* qian, Bing gets *c* qian, Ding gets *d* qian, Wu gets *e* qian.
"""

# 各列置本持錢數
本錢 = [20, 50, 40, 30, 60]

# 副併為法
法 = sum(本錢)

# 以利錢乘未併者
利錢 = 25635
實 = [利錢 * i for i in 本錢]

# 各自為實，實如法得一
a, b, c, d, e = [Fraction(i, 法) for i in 實]
"""
"""
