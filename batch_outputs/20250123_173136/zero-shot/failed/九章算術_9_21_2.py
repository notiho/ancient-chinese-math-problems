"""
有木去人不知遠近。立四表，相去各一丈，令左兩表與所望參相直。從後右表望之，入前右表三寸。問︰木去人幾何？
術曰：令一丈自乘為實，以三寸為法，實如法而一。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the distance of a tree from a person using geometric principles. Here's the Python code:


"""


from fractions import Fraction

# Given values
distance_between_poles = Fraction(1)  # 1丈
displacement = Fraction(3, 10)  # 3寸 = 3/10丈

# Calculation
a = (distance_between_poles ** 2) / displacement

# The result
a  # Distance of the tree from the person in 丈


"""


The variable `a` will hold the solution, which represents the distance of the tree from the person in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 10/3"""
