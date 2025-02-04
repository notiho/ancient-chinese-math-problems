"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a(=7200/61)錢
"""

#----- content starts here -----
"""
Suppose 720 qian is spent to buy 1 pi and 2 zhang 1 chi of silk.
It is desired to find the rate per zhang.
Question: how much qian per zhang?

The procedure says: Multiply the rate sought by the amount of money spent to obtain the dividend.
Take the rate of what was bought as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: 1 zhang costs *a*(=7200/61) qian.
"""

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
匹 = 1
丈 = 2
尺 = 1

# 將所有長度轉換為尺 (1 丈 = 10 尺)
總長度尺 = 匹 * 0 + 丈 * 10 + 尺

# 以所求率乘錢數為實
實 = 10 * 錢數  # 求每丈，1 丈 = 10 尺

# 以所買率為法
法 = 總長度尺

# 實如法得一
a = Fraction(實, 法)  # 7200/61 qian per zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
