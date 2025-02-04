"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
It is desired to find the price per bolt of cloth.
Question: how much qian per bolt?

The procedure says: Multiply the quantity being sought (price per bolt) by the total expenditure to obtain the dividend.
Take the total quantity of cloth purchased as the divisor.
Divide the dividend by the divisor to obtain the price per bolt.

Answer: one bolt costs *a* qian.
"""

from fractions import Fraction

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
布長度 = 2 * 10 + 7  # Convert 2 zhang 7 chi to total chi (1 zhang = 10 chi)

# 所買率為法 (total quantity of cloth purchased)
法 = 匹數

# 所求率乘錢數為實
實 = 錢數

# 實如法得一 (price per bolt)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
