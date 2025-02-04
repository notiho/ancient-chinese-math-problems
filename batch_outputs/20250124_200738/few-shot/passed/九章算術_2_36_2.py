"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,670 qian to purchase 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the price per shi. 
Question: how much qian per shi?

The procedure says: Multiply the rate being sought by the amount of money to obtain the dividend.
Use the rate of the purchased quantity as the divisor.
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
所求率 = 1 * 4 * 30  # 1 石 = 4 鈞 = 120 斤
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 每石的錢數#----- content ends here -----

"""
"""
