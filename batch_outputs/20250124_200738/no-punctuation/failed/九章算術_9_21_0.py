"""
有木去人不知遠近立四表相去各一丈令左兩表與所望參相直從後右表望之入前右表三寸問木去人幾何
術曰令一丈自乘為實以三寸為法實如法而一
荅曰 a丈 
"""

#----- content starts here -----
"""
There is a tree at an unknown distance from a person. Four poles are set up, each one zhang apart from the next. 
The left two poles and the tree are aligned in a straight line. 
From the rear right pole, the tree is observed to align with the front right pole, but it appears offset by 3 cun.
Question: how far is the tree from the person?

The procedure says: Take one zhang, square it to obtain the dividend.
Take 3 cun as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: the tree is *a* zhang away.
"""

# 令一丈自乘為實
一丈 = 1  # in zhang
實 = 一丈 ** 2

# 以三寸為法
三寸 = Fraction(3, 10)  # Convert 3 cun to zhang (1 zhang = 10 cun)
法 = 三寸

# 實如法而一
a = Fraction(實, 法)  # Result in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
