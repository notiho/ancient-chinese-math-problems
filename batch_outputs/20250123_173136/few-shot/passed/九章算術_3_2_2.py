"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian. 
The three of them together pass through a checkpoint, and the checkpoint tax is 100 qian.
It is desired to divide the tax proportionally according to the amount of money each holds.
Question: how much does each person pay?

The procedure says: Place the amounts of money each holds in a sequence of decreasing values.
Add these together to obtain the divisor.
Multiply the checkpoint tax (100 qian) by the amounts that have not been added together, obtaining the dividends.
Divide each dividend by the divisor to obtain the amount each person pays.

The answer says: Jia pays *a* qian, Yi pays *b* qian, and Bing pays *c* qian.
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
實 = [關稅 * 錢 for 錢 in 錢數]

# 實如法得一錢
a, b, c = [Fraction(錢, 法) for 錢 in 實]
"""
"""
