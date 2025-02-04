"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤銖率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a鈞 ， b銖 一錢。 其 c石 ， d銖 一錢。
"""

"""
To solve this problem, I need to break it down step by step according to the ancient Chinese mathematical procedure ("術"). Here's the Python code:


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

# Convert all units of silk to 銖 (smallest unit)
絲總銖 = (絲_石 * 120 * 16 * 24) + (絲_鈞 * 16 * 24) + (絲_斤 * 24) + (絲_兩 * 24 // 16) + 丝_銖

# 貴賤銖率之: 求每銖的價格
銖率 = Fraction(錢數, 絲總銖)

# 反其率術曰：以錢數為法，所率為實
法 = 錢數
實 = 絲總銖

# 實如法而一 (銖率已經計算完成)

# 不滿法者反以實減法，法少，實多
# This step is already implicit in the calculation of 銖率

# 二物各以所得多少之數乘法實，即物數
# Calculate the amount of silk in 鈞 and 銖
a = Fraction(絲總銖, 16 * 24)  # 鈞
b = Fraction(絲總銖 % (16 * 24), 24)  # 銖

# Convert 鈖 back to 石 and 銖
c = a // (120 * 16 * 24)  # 石
d = a % (120 * 16 * 24)  # Remaining 銖

print(f"其 {a} 鈞，{b} 銖 一錢。其 {c} 石，{d} 銖 一錢。")
#----- content ends here -----


"""


This code follows the ancient procedure step by step to calculate the price per 銖 and then distribute the total silk into 鈞 and 銖. Note that the units are carefully converted and handled throughout the calculation.
"""


"""
Code error: name '丝_銖' is not defined"""
