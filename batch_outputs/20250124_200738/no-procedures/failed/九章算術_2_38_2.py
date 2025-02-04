"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

#----- content starts here -----
"""
Suppose 1120 qian is spent to buy 1 shi, 2 jun, and 18 jin of silk.  
It is desired to calculate the price per jin (by weight) for both jun and shi.  
Question: What is the price per jin for each?

Answer: For 1 jun, each jin costs *a* qian.  
For 1 shi, each jin costs *b* qian.  
"""

# Total money spent
total_money = 1120

# Total weight in jin (1 shi = 120 jin, 1 jun = 30 jin)
total_weight = 1 * 120 + 2 * 30 + 18

# Price per jin
price_per_jin = Fraction(total_money, total_weight)

# For 1 jun (30 jin), price per jin
a = price_per_jin

# For 1 shi (120 jin), price per jin
b = price_per_jin

# Results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 560/99
Variable 'b' has wrong value. Expected: 5, Actual: 560/99
Missing variable in output: 'c'
Missing variable in output: 'd'"""
