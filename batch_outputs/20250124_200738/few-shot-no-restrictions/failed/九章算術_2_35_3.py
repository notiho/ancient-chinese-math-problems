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

The procedure says: Multiply the desired rate (price per bolt) by the total money spent to obtain the dividend.
Use the total quantity of cloth purchased as the divisor.
Perform the division to obtain the price per bolt.

Answer: one bolt costs *a* qian.
"""

from fractions import Fraction

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
布長度 = 2 * 10 + 7  # 2丈7尺 converted to 尺 (1丈 = 10尺)

# 每匹布的長度不影響價格計算，僅匹數 relevant
# 所買率為法
法 = 匹數

# 所求率乘錢數為實
實 = 錢數

# 實如法得一
a = Fraction(實, 法)

# Output result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
