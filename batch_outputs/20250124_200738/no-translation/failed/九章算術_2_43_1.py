"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To translate the problem into Python code, we need to carefully follow the ancient Chinese procedure ("術"). Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
絲_石 = 1
絲_鈞 = 2
絲_斤 = 28
絲_兩 = 3
絲_銖 = 5

# 將所有絲的重量轉換為銖 (1石 = 20鈞, 1鈞 = 30斤, 1斤 = 16兩, 1兩 = 24銖)
總銖 = (絲_石 * 20 * 30 * 16 * 24) + (絲_鈞 * 30 * 16 * 24) + (絲_斤 * 16 * 24) + (絲_兩 * 24) + 丝_銖

# 以錢數為法
法 = 錢數

# 所率為實
實 = 總銖

# 實如法而一 (計算每銖的價格)
每銖價格 = Fraction(法, 實)

# 不滿法者反以實減法，法少，實多 (反其率)
反率 = Fraction(實, 法)

# 計算各部分重量的價格
a = 每銖價格 * (2 * 30 * 16 * 24)  # 2鈞的價格
b = 每銖價格 * 1                   # 1銖的價格

c = 每銖價格 * (1 * 20 * 30 * 16 * 24)  # 1石的價格
d = 每銖價格 * 1                        # 1銖的價格
#----- content ends here -----


"""


This code follows the ancient procedure step by step, converting the weights into the smallest unit (銖), calculating the rate per 銖, and then determining the prices for the specified weights.
"""


"""
Code error: name '丝_銖' is not defined"""
