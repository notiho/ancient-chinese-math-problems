"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一石， a錢
"""

#----- content starts here -----
"""
Suppose there is 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
Question: what is the price per shi?

The procedure says: Multiply the amount of money by the rate you are seeking to obtain the dividend.
Use the total amount purchased as the divisor.
Divide the dividend by the divisor to obtain the price per shi.

Answer: 1 shi costs *a* qian.
"""

from fractions import Fraction

# 出錢一萬三千六百七十
錢數 = 13670

# 買絲一石二鈞一十七斤
# 1 石 = 4 鈞, 1 鈞 = 30 斤
石 = 1
鈞 = 2
斤 = 17
所買率 = 石 * 120 + 鈞 * 30 + 斤  # Convert everything to jin

# 以所求率乘錢數為實
實 = 錢數 * 120  # Convert to the rate for 1 shi (120 jin)

# 實如法得一
a = Fraction(實, 所買率)

# Output the result
a#----- content ends here -----

"""
"""
