"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

#----- content starts here -----
"""
Suppose there is a total payment of 13,970 qian to purchase silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and per jun.

Answer:
The price per jun is *a* qian.
The price per shi is *b* qian.
The price for *c* shi is *d* qian.
"""

# Total payment in qian
total_payment = 13970

# Total weight in jin (1 shi = 120 jin, 1 jun = 30 jin, 1 liang = 1/16 jin, 1 zhu = 1/384 jin)
total_weight_in_jin = (
    1 * 120 +  # 1 shi
    2 * 30 +   # 2 jun
    28 +       # 28 jin
    Fraction(3, 16) +  # 3 liang
    Fraction(5, 384)   # 5 zhu
)

# Price per jin
price_per_jin = Fraction(total_payment, total_weight_in_jin)

# Convert to price per jun (1 jun = 30 jin)
a = price_per_jin * 30

# Convert to price per shi (1 shi = 120 jin)
b = price_per_jin * 120

# Example: Calculate price for c shi (e.g., c = 2 shi)
c = 2
d = b * c

# Final results
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 8051, Actual: 643737600/79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 2
Variable 'd' has wrong value. Expected: 8052, Actual: 1287475200/79949"""
