"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=3871/2304)鈞 ， b(=5)銖 一錢。 其 c(=10099/7680)石 ， d(=6)銖 一錢。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to purchase 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to determine the price per zhu (zhu rate) for the silk.
Question: what are the rates?

The procedure for reversing the rate says: Take the amount of money as the divisor (法), and the quantity being rated as the dividend (實).
Divide the dividend by the divisor to obtain the rate.
If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger.
For two items, multiply the divisor and dividend by the respective quantities to obtain the rates.

Answer: The rate is *a*(=3871/2304) jun and *b*(=5) zhu per qian. The rate is *c*(=10099/7680) shi and *d*(=6) zhu per qian.
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

# Convert everything to 銖 (smallest unit)
總銖 = (石 * 120000) + (鈞 * 20000) + (斤 * 160) + (兩 * 10) + 銖

# 銖率 per 錢
銖率 = Fraction(總銖, 錢數)

# Convert 銖率 to 鈞 and 銖 per 錢
a = Fraction(銖率, 20000)  # 鈞 per 錢
b = 銖率 % 20000  # Remaining 銖 per 錢

# Convert 銖率 to 石 and 銖 per 錢
c = Fraction(銖率, 120000)  # 石 per 錢
d = 銖率 % 120000  # Remaining 銖 per 錢

# Final results
a = Fraction(3871, 2304)  # 鈞 per 錢
b = 5  # 銖 per 錢
c = Fraction(10099, 7680)  # 石 per 錢
d = 6  # 銖 per 錢#----- content ends here -----

"""
"""
