"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
Suppose there is 1120 qian spent to buy 1 shi, 2 jun, and 18 jin of silk.  
It is desired to calculate the price per jin (斤) based on the weight.  
Question: What is the price per jin for each jun (鈞) and each shi (石)?

Answer: For each jun, the price per jin is *a* qian.  
For each shi, the price per jin is *b* qian.
"""

# Total money spent
總錢 = 1120

# Total weight in jin (1 石 = 120 斤, 1 鈞 = 30 斤)
總重量 = 1 * 120 + 2 * 30 + 18

# Price per jin
每斤價格 = Fraction(總錢, 総重量)

# Price per jun (1 鈞 = 30 斤)
a = 每斤價格 * 30

# Price per shi (1 石 = 120 斤)
b = 每斤價格 * 120
"""
Code error: name '総重量' is not defined"""
