"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a(=100/3)丈 。
"""

#----- content starts here -----
"""
There is a tree, and its distance from a person is unknown. Four poles are erected, each one zhang apart from the next. 
The left two poles and the tree are aligned in a straight line. 
From the rear right pole, the tree is observed to deviate by three cun from the front right pole. 
Question: how far is the tree from the person?

The procedure says: Take one zhang, square it to obtain the dividend. 
Take three cun as the divisor. 
Divide the dividend by the divisor to obtain the result.

Answer: *a*(=100/3) zhang.
"""

# 相去各一丈
一丈 = 1

# 入前右表三寸
三寸 = Fraction(3, 10)  # Convert 3 cun to zhang (1 zhang = 10 cun)

# 令一丈自乘為實
實 = 一丈 * 一丈

# 以三寸為法
法 = 三寸

# 實如法而一
a = Fraction(實, 法)  # 100/3 zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
