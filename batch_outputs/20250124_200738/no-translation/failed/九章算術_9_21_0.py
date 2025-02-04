"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a丈 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 表相去各一丈
表距 = 1  # 丈

# 入前右表三寸
入表 = Fraction(3, 10)  # 將寸轉換為丈

# 令一丈自乘為實
實 = 表距 * 表距

# 以三寸為法
法 = 入表

# 實如法而一
a = Fraction(實, 法)
#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
