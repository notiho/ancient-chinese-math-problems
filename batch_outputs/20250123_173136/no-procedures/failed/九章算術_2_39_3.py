"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
Suppose there is a total of 13,970 qian spent to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and per jun.

Answer:
The price per jun is *a* qian.
The price per shi is *b* qian.
The price for c shi is *d* qian.
"""

# Total money spent
total_money = 13970

# Total weight in jin (1 shi = 120 jin, 1 jun = 30 jin, 1 jin = 16 liang, 1 liang = 24 zhu)
total_weight_in_jin = (
    1 * 120 +  # 1 shi
    2 * 30 +   # 2 jun
    28 +       # 28 jin
    Fraction(3, 16) +  # 3 liang (1 jin = 16 liang)
    Fraction(5, 384)   # 5 zhu (1 jin = 16 liang, 1 liang = 24 zhu, so 1 jin = 384 zhu)
)

# Price per jin
price_per_jin = Fraction(total_money, total_weight_in_jin)

# Convert price per jin to price per jun (1 jun = 30 jin)
a = price_per_jin * 30  # Price per jun in qian

# Convert price per jin to price per shi (1 shi = 120 jin)
b = price_per_jin * 120  # Price per shi in qian

# Example: Calculate price for c shi (e.g., 2 shi)
c = 2  # Example: 2 shi
d = b * c  # Price for c shi in qian

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 8051, Actual: 643737600/79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 2
Variable 'd' has wrong value. Expected: 8052, Actual: 1287475200/79949"""
