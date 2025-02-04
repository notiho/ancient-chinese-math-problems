"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=3871/2304)鈞 ， b(=5)銖 一錢。 其 c(=10099/7680)石 ， d(=6)銖 一錢。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per zhu. Question: what are the rates for each unit?

The procedure for reversing the rate says: Take the amount of money as the divisor, and the quantity being rated as the dividend.
Divide the dividend by the divisor to obtain the rate per unit.
If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger.
For two items, multiply the obtained rate by the total amount of money to calculate the quantity of each item.

Answer: The rate per jun is *a*(=3871/2304) zhu per qian, and *b*(=5) zhu per qian.
The rate per shi is *c*(=10099/7680) zhu per qian, and *d*(=6) zhu per qian.
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

# Convert everything to 銖 (1 石 = 120 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
總銖數 = (石 * 120 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 以錢數為法，所率為實
法 = 錢數
實 = 總銖數

# 實如法而一
銖率 = Fraction(實, 法)

# Convert 銖率 to 鈞 and 石 rates
# 1 鈞 = 30 斤 * 16 兩 * 24 銖 = 11520 銖
鈞率 = Fraction(銖率, 11520)

# 1 石 = 120 鈞 * 11520 銖 = 1382400 銖
石率 = Fraction(銖率, 1382400)

# Extract integer and fractional parts for 鈞 and 石 rates
a = 鈞率.numerator
b = 鈞率.denominator

c = 石率.numerator
d = 石率.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 1416269
Variable 'b' has wrong value. Expected: 5, Actual: 160934400
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 1416269
Variable 'd' has wrong value. Expected: 6, Actual: 19312128000"""
