"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian.
Together, they must pay a border tax of 100 qian.
It is desired to divide the tax proportionally according to the amount of money each holds.
Question: how much does each person pay?

The procedure says: Place each person's amount of money in a sequence as the decreasing sequence.
Add them together to obtain the divisor.
Multiply the tax (100 qian) by each person's amount of money (before summing), obtaining the dividend for each.
Divide the dividend by the divisor to obtain the amount each person pays.

Answer: Jia pays *a* qian, Yi pays *b* qian, and Bing pays *c* qian.
"""

# 甲持錢五百六十
甲 = 560

# 乙持錢三百五十
乙 = 350

# 丙持錢一百八十
丙 = 180

# 關稅百錢
關稅 = 100

# 各置錢數為列衰
錢數 = [甲, 乙, 丙]

# 副并為法
法 = sum(錢數)

# 以百錢乘未并者，各自為實
實_甲 = 關稅 * 甲
實_乙 = 關稅 * 乙
實_丙 = 關稅 * 丙

# 實如法得一錢
a = Fraction(實_甲, 法)
b = Fraction(實_乙, 法)
c = Fraction(實_丙, 法)
"""
"""
