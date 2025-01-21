"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

"""

"""


from fractions import Fraction

# 五日織通五尺
總織 = 5 * 10  # 將尺轉為寸

# 日自倍，列置衰副
列 = [1, 2, 4, 8, 16]

# 并得三十一為法
法 = sum(列)

# 以五尺乘并者，各自為實
實 = [總織 * i for i in列]

# 實如法而一，即得
初日 = Fraction(實[0], 法)
次日 = Fraction(實[1], 法)
三日 = Fraction(實[2], 法)
四日 = Fraction(實[3], 法)
五日 = Fraction(實[4], 法)

# 將結果轉為尺和寸
a = 初日  # 初日織 a 寸
b = 次日  # 次日織 b 寸
c = 三日  # 次日織 c 寸
d = 四日 // 10  # 四日織 d 尺
e = 五日

"""

"""


"""
Code error: invalid syntax. Perhaps you forgot a comma? (<string>, line 15)"""
