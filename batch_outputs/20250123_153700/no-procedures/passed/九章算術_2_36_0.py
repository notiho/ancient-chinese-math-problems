"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
荅曰：一石， a錢
"""

"""
Suppose there is a total of 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
Question: what is the price per shi (stone) of silk?

Answer: 1 shi costs *a* qian.
"""

# 出錢總數
總錢 = 13670

# 買絲的重量
# 1 石 = 120 斤, 1 鈞 = 30 斤
絲重量 = 1 * 120 + 2 * 30 + 17  # Convert everything to jin

# 每石的價格
# Convert the total weight to shi (divide by 120 jin per shi)
絲重量石 = Fraction(絲重量, 120)

# Calculate the price per shi
a = Fraction(總錢, 絲重量石)  # Total money divided by total weight in shi

a
"""
"""
