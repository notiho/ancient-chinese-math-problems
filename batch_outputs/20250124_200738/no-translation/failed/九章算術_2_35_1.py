"""
今有出錢二千三百七十，買布九匹二丈七尺。欲匹率之，問︰匹幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一匹， a錢
"""

"""

"""

#----- content starts here -----

# 出錢二千三百七十
錢數 = 2370

# 買布九匹二丈七尺
匹數 = 9
丈數 = 2
尺數 = 7

# 將丈數轉換為尺數 (1 丈 = 10 尺)
總尺數 = (匹數 * 10) + (丈數 * 10) + 尺數

# 以所求率乘錢數為實
實 = 錢數 * 1  # 所求率為 1 匹

# 以所買率為法
法 = 總尺數

# 實如法得一
a = Fraction(實, 法)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/39"""
