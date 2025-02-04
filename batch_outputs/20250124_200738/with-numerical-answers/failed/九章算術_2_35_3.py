"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a(=31600/129)錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth and 2 zhang 7 chi in total.
It is desired to find the price per bolt of cloth.
Question: how much is one bolt?

The procedure says: Multiply the rate to be sought by the amount of money spent, obtaining the dividend.
Take the rate of what was bought as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: one bolt costs *a*(=31600/129) qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
布長 = 2 * 10 + 7  # 2丈7尺 = 27尺

# 所買率為法
所買率 = 匹數 * 布長  # 9匹 × 27尺 = 243尺

# 以所求率乘錢數為實
實 = 錢數 * 布長  # 2370 × 27

# 實如法得一
a = Fraction(實, 所買率)  # 31600/129 qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
