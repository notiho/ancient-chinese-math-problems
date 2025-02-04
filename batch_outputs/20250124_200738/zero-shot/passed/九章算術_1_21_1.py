"""
今有田廣三步、三分步之一，從五步、五分步之二。問：為田幾何？
大廣田術曰：分母各乘其全，分子從之，相乘為實。分母相乘為法。實如法而一。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's how it can be done:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
田廣 = Fraction(3, 1) + Fraction(1, 3)  # 3步 + 1/3步
從田 = Fraction(5, 1) + Fraction(2, 5)  # 5步 + 2/5步

# The total area of the field
a = 田廣 * 從田

# The result
a  # a步
#----- content ends here -----


"""


Explanation:
1. The problem describes a rectangular field where the width (田廣) is `3步` plus `1/3步`, and the length (從田) is `5步` plus `2/5步`.
2. To find the total area of the field, we multiply the width by the length.
3. The result is stored in the variable `a`, which represents the area in "步".

Let me know if you'd like further clarification!
"""


"""
"""
