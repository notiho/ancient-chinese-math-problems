"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a丈 。
"""

"""
There is a tree, and its distance from a person is unknown. Four poles are set up, each one zhang apart from the next. 
The left two poles are aligned with the tree in a straight line. 
From the rear right pole, the tree is observed to be offset by 3 cun when viewed through the front right pole.
Question: how far is the tree from the person?

The procedure says: Take one zhang, square it to obtain the dividend. 
Take 3 cun as the divisor. 
Divide the dividend by the divisor to obtain the result.

Answer: the tree is *a* zhang away.
"""

# 相去各一丈
丈 = 1  # Distance between poles in zhang

# 入前右表三寸
寸 = 3  # Offset in cun

# 令一丈自乘為實
實 = 丈 * 丈

# 以三寸為法
法 = 寸

# 實如法而一
a = Fraction(實, 法)  # Result in zhang
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 1/3"""
