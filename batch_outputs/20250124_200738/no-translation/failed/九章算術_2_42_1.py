"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit of weight (石, 鈞, 斤, 兩, 銖) based on the total cost and the total weight. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 各置所買石、鈞、斤、兩以為法
# 1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每銖價格 = Fraction(實, 総銖)

# 計算各單位的價格
a = 每銖價格 * (4 * 30 * 16 * 24)  # 每石價格
b = 每銖價格 * (16 * 24)           # 每兩價格
c = 每銖價格 * (30 * 16 * 24)      # 每鈞價格
d = 每銖價格 * 24                  # 每兩價格

# Output results
a石 = a
b錢 = b
c鈞 = c
d錢 = d
#----- content ends here -----


"""
 

This code calculates the price per 石, 鈞, and 兩 based on the given total cost and weight. The results are represented as fractions for precision.
"""


"""
Code error: name '総銖' is not defined"""
