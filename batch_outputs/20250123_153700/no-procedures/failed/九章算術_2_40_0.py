"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

"""
Suppose there is a total of 13,970 qian spent to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.  
It is desired to calculate the price per jin and per jun.

Answer: Each jin costs *a* qian, and each jun costs *b* qian.  
Each shi costs *c* qian, and each jun costs *d* qian.
"""

# Total money spent
total_qian = 13970

# Total weight in jin (1 shi = 120 jin, 1 jun = 30 jin, 1 liang = 1/16 jin, 1 zhu = 1/384 jin)
total_weight_in_jin = (
    1 * 120 +  # 1 shi
    2 * 30 +   # 2 jun
    28 +       # 28 jin
    Fraction(3, 16) +  # 3 liang
    Fraction(5, 384)   # 5 zhu
)

# Price per jin
a = Fraction(total_qian, total_weight_in_jin)

# Total weight in jun (1 shi = 4 jun)
total_weight_in_jun = (
    1 * 4 +  # 1 shi
    2 +      # 2 jun
    Fraction(28, 30) +  # 28 jin
    Fraction(3, 480) +  # 3 liang (30 * 16 = 480)
    Fraction(5, 11520)  # 5 zhu (30 * 384 = 11520)
)

# Price per jun
b = Fraction(total_qian, total_weight_in_jun)

# Price per shi (1 shi = 120 jin)
c = Fraction(total_qian, 1)

# Price per jun (1 shi = 4 jun)
d = Fraction(total_qian, 4)

# Results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 160934400/79949
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 13970
Variable 'd' has wrong value. Expected: 2013, Actual: 6985/2"""
