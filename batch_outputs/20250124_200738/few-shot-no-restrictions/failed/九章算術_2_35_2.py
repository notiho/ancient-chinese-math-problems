"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts and 2 zhang 7 chi of cloth.
It is desired to calculate the price per bolt of cloth.
Question: how much qian per bolt?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Take the rate of the total purchase as the divisor.
Divide the dividend by the divisor to obtain the price per bolt.

Answer: one bolt costs *a* qian.
"""

from fractions import Fraction

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
布長 = 2 * 10 + 7  # 2丈7尺 converted to 尺 (1丈 = 10尺)

# 所買率 = 匹數
所買率 = 匹數

# 以所求率乘錢數為實
實 = 錢數

# 實如法得一
a = Fraction(實, 所買率)

# Answer
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
