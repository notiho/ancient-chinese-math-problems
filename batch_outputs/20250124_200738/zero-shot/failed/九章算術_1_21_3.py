"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will use the method described in the problem statement. The problem involves adding two fractional areas of land. Here's the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
area1 = Fraction(3, 1) + Fraction(1, 3)  # 3步, 3分步之一
area2 = Fraction(5, 1) + Fraction(2, 5)  # 5步, 5分步之二

# Total area
a = area1 + area2

# Result
a  # The total area in steps
#----- content ends here -----


"""


The variable `a` will contain the total area in steps as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 131/15"""
