"""
今有甲持錢二十乙持錢五十丙持錢四十丁持錢三十戊持錢六十凡五人合本治生得利二萬五千六百三十五欲以本錢多少分之問各人得幾何
術曰各列置本持錢數副併為法以利錢乘未併者各自為實實如法得一
答曰甲得 a錢 乙得 b錢 丙得 c錢 丁得 d錢 戊得 e錢
"""

"""
Suppose there are five people: Jia holds 20 qian, Yi holds 50 qian, Bing holds 40 qian, Ding holds 30 qian, and Wu holds 60 qian.
Together, they pool their capital and earn a profit of 25,635 qian.
Question: how much does each person receive based on their respective contributions?

The procedure says: List the amounts of capital held by each person.
Add them together to form the divisor.
Multiply the profit by the individual amounts of capital (before summing them), forming the dividends.
Divide each dividend by the divisor to obtain the share for each person.

Answer: Jia receives *a* qian, Yi receives *b* qian, Bing receives *c* qian, Ding receives *d* qian, and Wu receives *e* qian.
"""

# 各列置本持錢數
本持錢數 = [20, 50, 40, 30, 60]

# 副併為法
法 = sum(本持錢數)

# 以利錢乘未併者
利錢 = 25635
實 = [利錢 * 本 for 本 in 本持錢數]

# 各自為實，實如法得一
a, b, c, d, e = [Fraction(本, 法) for 本 in 实]
"""
Code error: name '实' is not defined"""
