"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a(=31600/129)錢
"""

"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
It is desired to find the price per bolt of cloth.
Question: how much is the price per bolt?

The procedure says: Multiply the rate being sought by the total amount of money spent, obtaining the dividend.
Take the rate of the purchase as the divisor.
Divide the dividend by the divisor to obtain the price per bolt.

Answer: the price per bolt is *a*(=31600/129) qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
每匹長度 = 2 * 10 + 7  # 2丈7尺 = 27尺
所買率 = 匹數 * 每匹長度  # 總長度

# 以所求率乘錢數為實
所求率 = 每匹長度
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 31600/129 qian
"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
