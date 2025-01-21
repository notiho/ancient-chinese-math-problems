"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a(=31600/129)錢
"""

"""
Suppose there is an expenditure of 2370 qian to buy 9 pi and 2 zhang 7 chi of cloth.
It is desired to calculate the price per pi of cloth.
Question: how much qian per pi?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Take the rate of what was bought as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: the price per pi is *a*(=31600/129) qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
布長 = 2 * 10 + 7  # 2丈7尺 = 27尺
所買率 = 匹數 * 布長  # 所買率 = 匹數 × 每匹布的長度

# 以所求率乘錢數為實
所求率 = 布長  # 每匹布的長度
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 31600/129 qian per pi
"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
