"""
今有甲持錢二十乙持錢五十丙持錢四十丁持錢三十戊持錢六十凡五人合本治生得利二萬五千六百三十五欲以本錢多少分之問各人得幾何
術曰各列置本持錢數副併為法以利錢乘未併者各自為實實如法得一
答曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢
"""

"""
Suppose there are five individuals: Jia holds 20 qian, Yi holds 50 qian, Bing holds 40 qian, Ding holds 30 qian, and Wu holds 60 qian.
Together, they pool their capital to conduct a business and earn a profit of 25,635 qian.
Question: how much profit does each person receive, proportional to their initial capital?

The procedure says: List the amounts of capital each person holds.
Add these amounts together to form the divisor.
Multiply the total profit by the individual amounts of capital (not yet added together), forming the dividends.
Divide each dividend by the divisor to determine the share of profit for each person.

Answer: Jia receives *a* qian, Yi receives *b* qian, Bing receives *c* qian, Ding receives *d* qian, and Wu receives *e* qian.
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
