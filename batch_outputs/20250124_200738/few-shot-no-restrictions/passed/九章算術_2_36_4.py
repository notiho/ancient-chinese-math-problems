"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a錢
"""

#----- content starts here -----
"""
Suppose there is 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
Question: what is the price per shi?

The procedure says: Multiply the amount of money by the rate you are seeking to calculate the dividend.
Use the rate of the purchased amount as the divisor.
Divide the dividend by the divisor to obtain the price per shi.

Answer: 1 shi costs *a* qian.
"""

# 出錢一萬三千六百七十
錢數 = 13670

# 買絲一石二鈞一十七斤
石 = 1
鈞 = 2
斤 = 17

# 1 石 = 4 鈞, 1 鈞 = 30 斤
所買率 = 石 * 4 * 30 + 鈞 * 30 + 斤  # Convert to total jin

# 所求率 (1 石 = 120 斤)
所求率 = 120  # 1 石 in jin

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)

# Answer
a#----- content ends here -----

"""
"""
