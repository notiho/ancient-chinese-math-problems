"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=3871/2304)鈞 ， b(=5)銖 一錢。 其 c(=10099/7680)石 ， d(=6)銖 一錢。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to purchase silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to determine the price per zhu rate. 
Question: what are the rates for each unit?

The procedure for reversing the rate says: Take the amount of money as the divisor, and the quantity being rated as the dividend. 
Divide the dividend by the divisor to obtain the rate per unit. 
If the dividend does not fully divide the divisor, subtract the remainder from the divisor, making the divisor smaller and the dividend larger. 
For two items, multiply the obtained rate by the divisor and dividend to calculate the quantity.

Answer: The rate per zhu is *a*(=3871/2304) jun, *b*(=5) zhu per qian. 
The rate per zhu is *c*(=10099/7680) shi, *d*(=6) zhu per qian.
"""

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert all units to 銖
總銖 = (石 * 120000) + (鈞 * 20000) + (斤 * 160) + (兩 * 10) + 銖

# 以錢數為法
法 = 錢數

# 所率為實
實 = 總銖

# 實如法而一
銖率 = Fraction(實, 法)

# Convert 銖率 to 鈞 and 銖 per 錢
a = Fraction(銖率, 20000)  # 鈞 per 錢
b = 銖率 % 10  # 銖 per 錢

# Convert 銖率 to 石 and 銖 per 錢
c = Fraction(銖率, 120000)  # 石 per 錢
d = 銖率 % 10  # 銖 per 錢#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 32903/55880000
Variable 'b' has wrong value. Expected: 5, Actual: 4963/2794
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 32903/335280000
Variable 'd' has wrong value. Expected: 6, Actual: 4963/2794"""
