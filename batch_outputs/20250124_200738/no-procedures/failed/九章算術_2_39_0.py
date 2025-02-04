"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and per jun.

Answer: the price per jun is *a* qian, and the price per shi is *b* qian.
The price for c shi is *d* qian.
"""

# Total expenditure in qian
total_qian = 13970

# Total weight in jin
shi_to_jin = 120  # 1 shi = 120 jin
jun_to_jin = 30   # 1 jun = 30 jin
jin_to_liang = 16 # 1 jin = 16 liang
liang_to_zhu = 24 # 1 liang = 24 zhu

total_jin = (
    1 * shi_to_jin +  # 1 shi
    2 * jun_to_jin +  # 2 jun
    28 +              # 28 jin
    Fraction(3, jin_to_liang) +  # 3 liang
    Fraction(5, jin_to_liang * liang_to_zhu)  # 5 zhu
)

# Price per jin
price_per_jin = Fraction(total_qian, total_jin)

# Convert price per jin to price per jun and per shi
price_per_jun = price_per_jin * jun_to_jin
price_per_shi = price_per_jin * shi_to_jin

# Assign results
a = price_per_jun
b = price_per_shi

# Example: price for c shi (let's assume c = 2 shi)
c = 2
d = price_per_shi * c

# Results
a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 8051, Actual: 643737600/79949
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 2
Variable 'd' has wrong value. Expected: 8052, Actual: 1287475200/79949"""
