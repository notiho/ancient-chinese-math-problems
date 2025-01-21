"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
荅曰：一石， a錢
"""

"""
Suppose there is 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
Question: what is the cost per shi?

Answer: 1 shi costs *a* qian.
"""

# 出錢
錢 = 13670

# 買絲的重量：1石2鈞17斤
# 1 石 = 120 斤, 1 鈞 = 30 斤
重量 = 1 * 120 + 2 * 30 + 17  # Total weight in jin

# 石率 (cost per shi)
# Convert total weight into shi (1 shi = 120 jin)
重量_in_石 = Fraction(重量, 120)

# Calculate cost per shi
a = Fraction(錢, 重量_in_石)  # Cost per shi in qian

a
"""
"""
