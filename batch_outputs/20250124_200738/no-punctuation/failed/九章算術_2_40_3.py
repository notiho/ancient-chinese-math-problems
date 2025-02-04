"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤鈞率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a斤 鈞 b錢 其 c石 鈞 d錢 
"""

#----- content starts here -----
This problem is about determining the price per unit weight (jin and shi) for a given amount of money spent on silk. Let's break it down and encode the procedure step by step.

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: What is the price per jun and per shi?

The procedure says: Place the weights (shi, jun, jin, liang) as the divisor.
Multiply the total money by the weights to get the dividend.
Divide the dividend by the divisor to get the unit price.
If there is a remainder, subtract it from the divisor to adjust the calculation.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

Answer: The price per jun is *a* qian, and the price per shi is *c* qian.
"""

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert all weights to jin (1 石 = 120 斤, 1 鈞 = 30 斤, 1 兩 = 1/16 斤, 1 銖 = 1/384 斤)
總斤 = (石 * 120) + (鈞 * 30) + 斤 + Fraction(兩, 16) + Fraction(銖, 384)

# 以為法 (the total weight in jin is the divisor)
法 = 總斤

# 以所率乘錢數為實 (multiply the money by the weights to get the dividend)
實 = 錢數

# 實如法而一 (divide the dividend by the divisor to get the unit price per jin)
每斤價 = Fraction(實, 法)

# Convert the price per jin to price per jun (1 jun = 30 jin)
每鈞價 = 每斤價 * 30

# Convert the price per jin to price per shi (1 shi = 120 jin)
每石價 = 每斤價 * 120

# Output the results
a = 每鈞價
c = 每石價#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
