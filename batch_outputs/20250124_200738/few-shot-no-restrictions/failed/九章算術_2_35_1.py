"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

#----- content starts here -----
"""
Suppose there is 2370 qian spent to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
It is desired to calculate the price per bolt of cloth.
Question: how much qian per bolt?

The procedure says: Multiply the desired rate (in this case, per bolt) by the total money spent to obtain the dividend.
Use the total rate (in this case, the total number of bolts) as the divisor.
Divide the dividend by the divisor to obtain the price per bolt.

Answer: one bolt costs *a* qian.
"""

from fractions import Fraction

# 出錢二千三百七十
錢數 = 2370

# 買布九匹
匹數 = 9

# 匹率之
a = Fraction(錢數, 匹數)

# Answer
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
