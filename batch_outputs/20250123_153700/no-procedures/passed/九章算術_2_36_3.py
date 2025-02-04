"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
荅曰：一石， a錢
"""

"""
Suppose there is a total of 13,670 qian spent to buy 1 shi, 2 jun, and 17 jin of silk.
Question: What is the price per shi?

Answer: 1 shi costs *a* qian.
"""

# 出錢一萬三千六百七十
total_money = 13670

# 買絲一石二鈞一十七斤
# 1 石 = 4 鈞, 1 鈞 = 30 斤
total_weight_in_jin = (1 * 4 * 30) + (2 * 30) + 17

# Convert total weight to shi (1 石 = 120 斤)
total_weight_in_shi = Fraction(total_weight_in_jin, 120)

# 石率 (price per shi)
a = Fraction(total_money, total_weight_in_shi)

# Final result
a
"""
"""
