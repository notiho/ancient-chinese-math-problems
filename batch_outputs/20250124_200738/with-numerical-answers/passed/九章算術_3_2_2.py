"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a(=5600/109)錢 。乙出 b(=3500/109)錢 。丙出 c(=1800/109)錢 。
"""

#----- content starts here -----
"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian. 
Together, they need to pay a toll of 100 qian. 
It is desired to distribute the toll proportionally based on the amount of money each person holds.
Question: how much does each person pay?

The procedure says: Place the amounts of money each person holds in a sequence of decreasing values.
Add these amounts together to obtain the divisor.
Multiply the toll (100 qian) by the individual amounts of money (not yet summed), making each a dividend.
Divide each dividend by the divisor to obtain the amount each person pays.

Answer: Jia pays *a*(=5600/109) qian, Yi pays *b*(=3500/109) qian, and Bing pays *c*(=1800/109) qian.
"""

from fractions import Fraction

# 甲持錢五百六十
甲 = 560

# 乙持錢三百五十
乙 = 350

# 丙持錢一百八十
丙 = 180

# 各置錢數為列衰
錢數 = [甲, 乙, 丙]

# 副并為法
法 = sum(錢數)

# 以百錢乘未并者
關稅 = 100
實 = [關稅 * i for i in 錢數]

# 實如法得一錢
a, b, c = [Fraction(i, 法) for i in 實]  # 5600/109, 3500/109, 1800/109#----- content ends here -----

"""
"""
