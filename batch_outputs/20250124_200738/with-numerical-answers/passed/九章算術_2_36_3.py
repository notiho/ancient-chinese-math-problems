"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a(=1640400/197)錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,670 qian to purchase 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the rate per shi. 
Question: how many qian per shi?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Use the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: 1 shi costs *a*(=1640400/197) qian.
"""

# 出錢一萬三千六百七十
錢數 = 13670

# 買絲一石二鈞一十七斤
石 = 1
鈞 = 2
斤 = 17

# 1 石 = 120 斤, 1 鈞 = 30 斤
所買率 = 石 * 120 + 鈞 * 30 + 斤

# 以所求率乘錢數為實
所求率 = 120  # 求每石的錢數
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 1640400/197 qian#----- content ends here -----

"""
"""
