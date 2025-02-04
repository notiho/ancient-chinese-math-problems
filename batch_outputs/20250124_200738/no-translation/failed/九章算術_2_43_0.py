"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, we need to carefully follow the ancient Chinese mathematical procedure ("反其率術"). Here's how we can translate it into Python code:


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

# Convert the total weight of silk into 銖 (smallest unit)
# 1 石 = 20 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
絲_總銖 = (
    (絲_石 * 20 * 30 * 16 * 24) +
    (絲_鈞 * 30 * 16 * 24) +
    (絲_斤 * 16 * 24) +
    (絲_兩 * 24) +
    丝_銖
)

# 貴賤銖率之: 求每銖的價格
銖率 = Fraction(錢數, 絲_總銖)

# 反其率術: 計算各部分
# a鈞, b銖 一錢
a = 銖率.numerator // (30 * 16 * 24)  # 鈞
剩餘銖 = 銖率.numerator % (30 * 16 * 24)
b = 剩餘銖  # 銖

# c石, d銖 一錢
c = 銖率.numerator // (20 * 30 * 16 * 24)  # 石
剩餘銖_石 = 銖率.numerator % (20 * 30 * 16 * 24)
d = 剩餘銖_石  # 銖

# Output the results
print(f"其 {a} 鈞, {b} 銖 一錢。其 {c} 石, {d} 銖 一錢。")
#----- content ends here -----


"""


This code follows the ancient procedure step by step, converting the total weight into the smallest unit (銖), calculating the rate per 銖, and then determining the results in terms of 鈞 and 石.
"""


"""
Code error: name '丝_銖' is not defined"""
