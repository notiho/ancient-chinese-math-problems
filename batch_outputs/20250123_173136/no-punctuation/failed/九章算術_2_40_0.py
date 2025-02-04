"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤鈞率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a斤 鈞 b錢 其 c石 鈞 d錢 
"""

This problem involves calculating the price per unit weight (jin and jun) for silk based on the total cost and weight. Let's break it down step by step according to the procedure.

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: What is the price per jun and per jin?

The procedure says: Place the total weight in shi, jun, jin, liang, and zhu as the divisor.
Multiply the total money by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the price per unit.
If the remainder is less than the divisor, subtract the remainder from the divisor.
The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

Answer: The price per jin is *a* qian and *b* fen. The price per jun is *c* qian and *d* fen.
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

# Convert everything to 銖 (the smallest unit)
# 1 石 = 1200 斤 = 384000 銖
# 1 鈞 = 100 斤 = 32000 銖
# 1 斤 = 16 兩 = 160 銖
# 1 兩 = 10 銖
總銖 = 石 * 384000 + 鈞 * 32000 + 斤 * 160 + 兩 * 10 + 銖

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每銖價格 = Fraction(實, 総銖)

# Convert the price per 銖 back to 鈞 and 斤
# 1 鈞 = 32000 銖
每鈞價格 = 每銖價格 * 32000

# 1 斤 = 160 銖
每斤價格 = 每銖價格 * 160

# Extract the integer and fractional parts for 鈞 and 斤 prices
a = 每斤價格.numerator // 每斤價格.denominator  # Price per 斤 in qian
b = 每斤價格 - a  # Fractional part of price per 斤

c = 每鈞價格.numerator // 每鈞價格.denominator  # Price per 鈞 in qian
d = 每鈞價格 - c  # Fractional part of price per 鈞

a = Fraction(a)
b = Fraction(b)
c = Fraction(c)
d = Fraction(d)
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
