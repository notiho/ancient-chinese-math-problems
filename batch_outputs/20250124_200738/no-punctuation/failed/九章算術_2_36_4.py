"""
今有出錢一萬三千六百七十買絲一石二鈞一十七斤欲石率之問石幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一石 a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,670 qian to buy 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the rate per shi.
Question: how many qian per shi?

The procedure says: Multiply the rate sought by the amount of money spent, obtaining the dividend.
Take the rate of what was bought as the divisor.
Divide the dividend by the divisor, obtaining the rate per shi.

Answer: 1 shi costs *a* qian.
"""

# 出錢一萬三千六百七十
錢數 = 13670

# 所買絲 1 石 2 鈞 17 斤
石 = 1
鈞 = 2
斤 = 17

# 1 石 = 4 鈞, 1 鈞 = 30 斤
所買率 = 石 * 4 * 30 + 鈞 * 30 + 斤

# 以所求率乘錢數為實
實 = 錢數 * 1  # 所求率為 1 石

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 每石的錢數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1640400/197, Actual: 13670/197"""
