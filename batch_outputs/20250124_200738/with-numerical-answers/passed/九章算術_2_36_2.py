"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a(=1640400/197)錢
"""

#----- content starts here -----
"""
Suppose there is 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the price per shi. 
Question: how much qian per shi?

The procedure says: Multiply the desired rate (shi) by the total amount of money spent, obtaining the dividend.
Take the rate of the purchased amount as the divisor.
Divide the dividend by the divisor to obtain the price per shi.

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

# 所求率 (石) = 120 斤
所求率 = 120

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法) # 1640400/197 qian per shi#----- content ends here -----

"""
"""
