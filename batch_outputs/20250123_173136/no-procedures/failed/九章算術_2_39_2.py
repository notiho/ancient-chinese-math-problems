"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
Suppose there is a total of 13,970 qian spent to purchase 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per shi and per jun.

Answer:
The price per jun is *a* qian.
The price per shi is *b* qian.
The price for c shi is *d* qian.
"""

# Total money spent
total_qian = 13970

# Total weight in jin
shi_to_jin = 120  # 1 shi = 120 jin
jun_to_jin = 30   # 1 jun = 30 jin
liang_to_jin = Fraction(1, 16)  # 1 liang = 1/16 jin
zhu_to_jin = Fraction(1, 160)   # 1 zhu = 1/160 jin

total_weight_in_jin = (
    1 * shi_to_jin +
    2 * jun_to_jin +
    28 +
    3 * liang_to_jin +
    5 * zhu_to_jin
)

# Price per jin
price_per_jin = Fraction(total_qian, total_weight_in_jin)

# Price per jun (30 jin)
a = price_per_jin * 30

# Price per shi (120 jin)
b = price_per_jin * 120

# Example: Price for c shi (e.g., 2 shi)
c = 2
d = price_per_jin * (c * shi_to_jin)

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 4470400/2221
Variable 'b' has wrong value. Expected: 8051, Actual: 17881600/2221
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 2
Variable 'd' has wrong value. Expected: 8052, Actual: 35763200/2221"""
