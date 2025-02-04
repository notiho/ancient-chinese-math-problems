"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian.
In total, the three people pass through a checkpoint, and the checkpoint tax is 100 qian.
It is desired to divide the tax proportionally to the amount of money each person holds.
Question: how much does each person pay?

The procedure says: Place each person's amount of money in a sequence of decreasing values.
Add them together to form the divisor.
Multiply the tax (100 qian) by each person's amount of money (before summing), forming the dividend for each.
Divide the dividend by the divisor to obtain the amount each person pays.

Answer: Jia pays *a* qian, Yi pays *b* qian, and Bing pays *c* qian.
"""

# 各置錢數為列衰
甲錢 = 560
乙錢 = 350
丙錢 = 180

# 副并為法
法 = 甲錢 + 乙錢 + 丙錢

# 以百錢乘未并者，各自為實
稅 = 100
甲實 = 稅 * 甲錢
乙實 = 稅 * 乙錢
丙實 = 稅 * 丙錢

# 實如法得一錢
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)
"""
"""
