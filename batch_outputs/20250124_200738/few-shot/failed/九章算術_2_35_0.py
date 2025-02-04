"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
It is desired to find the price per bolt. 
Question: how much money per bolt?

The procedure says: Multiply the rate being sought by the total money spent to obtain the dividend.
Use the rate of what was bought as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: one bolt costs *a* qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
每匹長度 = 2 * 10 + 7  # 2丈 = 20尺, so 2丈7尺 = 27尺
所買率 = 匹數

# 以所求率乘錢數為實
實 = 錢數 * 1  # 所求率為每匹價格，默認為1匹

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(錢數, 匹數)  # 每匹價格#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
