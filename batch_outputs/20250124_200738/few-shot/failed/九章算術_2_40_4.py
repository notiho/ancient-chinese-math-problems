"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤鈞率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a斤 ，鈞 b錢 。其 c石 ，鈞 d錢 。
"""

#----- content starts here -----
This problem involves calculating the price per unit weight (jin and jun) for a given amount of money and silk. Let's break it down step by step according to the procedure.

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per jun and per jin.

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to obtain the price per unit.
If the divisor is not fully divisible, subtract the remainder from the divisor; the divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: The price per *a* jin is *b* qian. The price per *c* shi is *d* qian.
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

# Convert all weights to jin (1 shi = 120 jin, 1 jun = 30 jin, 1 liang = 1/16 jin, 1 zhu = 1/384 jin)
總斤 = 石 * 120 + 鈞 * 30 + 斤 + Fraction(兩, 16) + Fraction(銖, 384)

# Calculate the price per jin
價錢每斤 = Fraction(錢數, 總斤)

# Calculate the price per jun (1 jun = 30 jin)
價錢每鈞 = 價錢每斤 * 30

# Output results
a = 1  # Per jin
b = 價錢每斤
c = 1  # Per jun
d = 價錢每鈞#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
