"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a丈 。
"""

#----- content starts here -----
"""
There is a tree at an unknown distance from a person. Four poles are set up, each one zhang apart from the next. The left two poles are aligned with the tree as seen by the observer. From the rear right pole, the observer sees the front right pole shifted by 3 cun relative to the tree. 
Question: how far is the tree from the observer?

The procedure says: Take one zhang, square it to obtain the dividend. Use 3 cun as the divisor. Divide the dividend by the divisor to obtain the result.

Answer: the tree is *a* zhang away.
"""

from fractions import Fraction

# 相去各一丈
距離 = 1  # in zhang

# 入前右表三寸
偏移 = Fraction(3, 10)  # Convert 3 cun to zhang (1 zhang = 10 cun)

# 令一丈自乘為實
實 = 距離 ** 2

# 以三寸為法
法 = 偏移

# 實如法而一
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
