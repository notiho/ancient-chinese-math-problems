"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,670 qian to buy 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the price per shi. 
Question: how much qian per shi?

The procedure says: Multiply the desired rate (1 shi) by the total expenditure (qian), obtaining the dividend.
Take the rate of what was bought (1 shi, 2 jun, 17 jin) as the divisor.
Divide the dividend by the divisor, obtaining the price per shi.

Answer: 1 shi costs *a* qian.
"""

# 出錢一萬三千六百七十
錢數 = 13670

# 買絲一石二鈞一十七斤
石 = 1
鈞 = 2
斤 = 17

# 1 石 = 120 斤, 1 鈞 = 30 斤
所買率 = 石 * 120 + 鈞 * 30 + 斤

# 所求率 (1 石)
所求率 = 1 * 120  # 1 石 = 120 斤

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 每石的錢數#----- content ends here -----

"""
"""
