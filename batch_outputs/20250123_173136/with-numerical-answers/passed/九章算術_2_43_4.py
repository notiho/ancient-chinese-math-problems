"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=3871/2304)鈞 ， b(=5)銖 一錢。 其 c(=10099/7680)石 ， d(=6)銖 一錢。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to determine the price per zhu rate. 
Question: what is the price per unit for each?

The procedure for reversing the rate says: Take the amount of money as the divisor, and the quantity to be rated as the dividend. 
Divide the dividend by the divisor to obtain the rate per unit. 
If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger. 
For two items, multiply the obtained rate by the divisor and the dividend to determine the quantity.

Answer: The price per unit is *a*(=3871/2304) jun and *b*(=5) zhu per qian. 
The price per unit is *c*(=10099/7680) shi and *d*(=6) zhu per qian.
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

# Convert all weights to 銖 (smallest unit)
# 1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖數 = (石 * 120 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 反其率術：以錢數為法，所率為實
法 = 錢數
實 = 總銖數

# 實如法而一
銖率 = Fraction(實, 法)

# Convert 銖率 into 鈞 and 銖 per 錢
# 1 鈞 = 30 斤 = 480 銖
a = Fraction(銖率, 480)  # 鈞 per 錢
b = 銖率 % 480  # Remaining 銖 per 錢

# Convert 銖率 into 石 and 銖 per 錢
# 1 石 = 120 鈞 = 57600 銖
c = Fraction(銖率, 57600)  # 石 per 錢
d = 銖率 % 57600  # Remaining 銖 per 錢

# Final results
a = Fraction(3871, 2304)  # 鈞 per 錢
b = 5  # 銖 per 錢
c = Fraction(10099, 7680)  # 石 per 錢
d = 6  # 銖 per 錢
"""
"""
