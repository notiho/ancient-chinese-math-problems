"""
今有女子善織，日自倍，五日織通五尺。問：日織幾何？
術曰：各置列衰副，并得三十一為法，以五尺乘并者，各自為實，實如法而一，即得。
答曰：初日織 a寸 ，次日織 b寸 ，次日織 c寸 ，次日織 d尺 ，次日織 e尺 。
"""

"""

"""


from fractions import Fraction

# 五日織通五尺
總織 = 5 * 10  # 將尺轉為寸，1尺 = 10寸

# 日自倍，列置衰副
列 = [1, 2, 4, 8, 16]  # 每日織量倍增

# 并得三十一為法
法 = sum(列)

# 以五尺乘并者，各自為實
實 = [總織 * i for i in 列]

# 實如法而一，即得
a = Fraction(實[0], 法)  # 初日織 a 寸
b = Fraction(實[1], 法)  # 次日織 b 寸
c = Fraction(實[2], 法)  # 次日織 c 寸
d = Fraction(實[3], 法) // 10  # 次日織 d 尺
e = Fraction(實[4], 法) // 10  # 次日織 e 尺


"""
 

This code calculates the amount woven each day based on the given procedure. The results `a`, `b`, `c` are in "寸" (inches), while `d` and `e` are in "尺" (feet).
"""


"""
Variable 'd' has wrong value. Expected: 40/31, Actual: 1
Variable 'e' has wrong value. Expected: 80/31, Actual: 2"""
