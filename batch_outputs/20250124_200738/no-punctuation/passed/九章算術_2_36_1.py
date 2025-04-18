"""
今有出錢一萬三千六百七十買絲一石二鈞一十七斤欲石率之問石幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一石 a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,670 qian to purchase 1 shi, 2 jun, and 17 jin of silk.
It is desired to calculate the price per shi.
Question: how much is the price per shi?

The procedure says: Multiply the desired rate (1 shi) by the total money spent, obtaining the dividend.
Take the rate of the purchased amount as the divisor.
Divide the dividend by the divisor to obtain the price per shi.

The answer says: 1 shi costs *a* qian.
"""

# 出錢一萬三千六百七十
錢數 = 13670

# 所買絲一石二鈞一十七斤
石 = 1
鈞 = 2
斤 = 17

# 1 石 = 4 鈞, 1 鈞 = 30 斤
所買率 = 石 * 4 * 30 + 鈞 * 30 + 斤

# 所求率 1 石
所求率 = 1 * 4 * 30  # 1 石 in terms of 斤

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # Price per shi in qian#----- content ends here -----

"""
"""
