"""
今有出錢一萬三千六百七十，買絲一石二鈞一十七斤。欲石率之，問︰石幾何？
荅曰：一石， a錢
"""

"""
Suppose there is a total payment of 13,670 qian to buy 1 shi, 2 jun, and 17 jin of silk.
Question: what is the cost per shi?

Answer: 1 shi costs *a* qian.
"""

# Total payment in qian
total_payment = 13670

# Convert the weight into jin (1 shi = 120 jin, 1 jun = 20 jin)
weight_in_jin = 1 * 120 + 2 * 20 + 17

# Cost per jin
cost_per_jin = Fraction(total_payment, weight_in_jin)

# Convert cost per jin to cost per shi (1 shi = 120 jin)
a = cost_per_jin * 120
"""
Variable 'a' has wrong value. Expected: 1640400/197, Actual: 546800/59"""
