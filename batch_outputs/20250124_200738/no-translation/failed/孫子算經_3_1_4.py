"""
今有丁一千五百萬，出兵四十萬。問：幾丁科一兵？
術曰：置丁一千五百萬為實，以兵四十萬為法，實如法，即得。
答曰： a 丁 b分 。
"""

"""

"""

#----- content starts here -----

# 置丁一千五百萬為實
實 = 15000000

# 以兵四十萬為法
法 = 400000

# 實如法，即得
a = 實 // 法  # 整數部分
b = Fraction(實 % 法, 法)  # 餘數部分作為分數
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 5, Actual: 1/2"""
