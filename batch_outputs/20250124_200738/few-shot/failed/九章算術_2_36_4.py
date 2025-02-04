"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,670 qian to buy 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the rate per shi. 
Question: how many qian per shi?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Take the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: 1 shi costs *a* qian.
"""

# 出錢一萬三千六百七十
錢數 = 13670

# 買絲一石二鈞一十七斤
石 = 1
鈞 = 2
斤 = 17

# 1 石 = 4 鈞, 1 鈞 = 30 斤
所買率 = 石 * 4 * 30 + 鈞 * 30 + 斤

# 以所求率乘錢數為實
實 = 錢數 * 1  # 所求率 is 1 shi

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 每石的錢數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1640400/197, Actual: 13670/197"""
