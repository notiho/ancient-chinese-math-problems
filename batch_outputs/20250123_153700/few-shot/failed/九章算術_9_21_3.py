"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a丈 。
"""

"""
There is a tree at an unknown distance from a person. Four poles are set up, each one zhang apart from the next. 
The left two poles are aligned with the tree as seen from the observer's perspective. 
From the rear-right pole, the tree appears to shift inward by 3 cun relative to the front-right pole.
Question: how far is the tree from the observer?

The procedure says: Take one zhang and square it to obtain the dividend. 
Take 3 cun as the divisor. Divide the dividend by the divisor to obtain the result.

Answer: the tree is *a* zhang away.
"""

# 相去各一丈
一丈 = 1  # in zhang

# 入前右表三寸
三寸 = Fraction(3, 10)  # Convert cun to zhang (10 cun = 1 zhang)

# 令一丈自乘為實
實 = 一丈 * 一丈

# 以三寸為法
法 = 三寸

# 實如法而一
a = Fraction(實, 法)  # The distance to the tree in zhang
"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
