"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth, each 2 zhang and 7 chi in length.
It is desired to calculate the price per bolt.
Question: how much is one bolt?

The procedure says: Multiply the quantity sought (price per bolt) by the total expenditure to obtain the dividend.
Use the total quantity purchased as the divisor.
Divide the dividend by the divisor to obtain the price per bolt.

Answer: one bolt costs *a* qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
布長 = 2 * 10 + 7  # 2丈7尺 converted to chi

# 所買率為法
法 = 匹數

# 以所求率乘錢數為實
實 = 錢數

# 實如法得一
a = Fraction(實, 法)  # Price per bolt in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
