"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
荅曰：一石， a錢
"""

#----- content starts here -----
"""
Suppose there is 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
Question: what is the cost per shi?

Answer: 1 shi costs *a* qian.
"""

# 出錢
出錢 = 13670

# 買絲
絲_石 = 1  # 1 石
絲_鈞 = 2  # 2 鈞
絲_斤 = 17  # 17 斤

# Convert everything to jin (1 石 = 120 斤, 1 鈞 = 30 斤)
總斤 = (絲_石 * 120) + (絲_鈞 * 30) + 丝_斤

# Calculate the cost per jin
每斤價格 = Fraction(出錢, 總斤)

# Calculate the cost per 石 (1 石 = 120 斤)
a = 每斤價格 * 120#----- content ends here -----

"""
Code error: name '丝_斤' is not defined"""
