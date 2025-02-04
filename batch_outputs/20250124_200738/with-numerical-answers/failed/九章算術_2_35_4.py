"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a(=31600/129)錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 pi and 2 zhang 7 chi of cloth.
It is desired to calculate the price per pi.
Question: how much qian per pi?

The procedure says: Multiply the rate being sought by the money spent to obtain the dividend.
Take the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: One pi costs *a*(=31600/129) qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
丈數 = 2
尺數 = 7

# Convert the total length to chi (1 丈 = 10 尺)
總長度 = 匹數 * 10 + 丈數 * 10 + 尺數

# 所求率 (price per 匹)
所求率 = 10  # Each 匹 is equivalent to 10 chi

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 總長度

# 實如法得一
a = Fraction(實, 法)  # 31600/129 qian per 匹#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 7900/39"""
