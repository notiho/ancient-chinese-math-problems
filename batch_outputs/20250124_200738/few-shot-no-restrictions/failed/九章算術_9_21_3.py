"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a丈 。
"""

#----- content starts here -----
"""
There is a tree at an unknown distance from a person. Four poles are set up, each one zhang apart from the next. 
The left two poles are aligned with the tree as seen from the observer's perspective. 
From the rear right pole, the tree appears to be offset by 3 cun when viewed past the front right pole.
Question: how far is the tree from the observer?

The procedure says: Take one zhang, square it to obtain the dividend. Use 3 cun as the divisor. Divide the dividend by the divisor to obtain the result.

Answer: the tree is *a* zhang away.
"""

from fractions import Fraction

# 相去各一丈
距離_丈 = 1  # 1 丈

# 入前右表三寸
偏移_寸 = 3  # 3 寸

# 令一丈自乘為實
實 = 距離_丈 ** 2

# 以三寸為法
法 = Fraction(偏移_寸, 10)  # 1 丈 = 10 寸, so convert 3 寸 to 丈

# 實如法而一
a = Fraction(實, 法)

# Output the result
a  # The tree is `a` zhang away.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
