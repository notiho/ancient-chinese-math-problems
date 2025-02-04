"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

#----- content starts here -----
"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian. 
In total, the three people are traveling together and need to pay a border tax of 100 qian.
The tax should be divided proportionally based on the amount of money each person holds.
Question: how much does each person pay?

The procedure says: Place the amounts of money each person holds in a sequence as the proportional weights.
Add these amounts together to form the divisor.
Multiply the tax (100 qian) by each person's amount of money (not yet summed), forming the dividend for each.
Divide each dividend by the divisor to obtain the amount each person pays.

Answer: Jia pays *a* qian, Yi pays *b* qian, and Bing pays *c* qian.
"""

from fractions import Fraction

# 各置錢數為列衰
甲錢 = 560
乙錢 = 350
丙錢 = 180

# 副并為法
法 = 甲錢 + 乙錢 + 丙錢

# 稅金
稅金 = 100

# 以百錢乘未并者，各自為實
甲實 = 稅金 * 甲錢
乙實 = 稅金 * 乙錢
丙實 = 稅金 * 丙錢

# 實如法得一錢
a = Fraction(甲實, 法)
b = Fraction(乙實, 法)
c = Fraction(丙實, 法)

# Output the results
a, b, c#----- content ends here -----

"""
"""
