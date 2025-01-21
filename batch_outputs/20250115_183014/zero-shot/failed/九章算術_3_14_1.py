"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a proportional relationship between silk and a finished product (縑). Here's the Python code:


"""


from fractions import Fraction

# Given values
silk_1 = Fraction(14)  # 14斤
product_1 = Fraction(10)  # 10斤

silk_2 = Fraction(45, 2)  # 45斤8兩 = 45.5斤

# Calculation
a = (product_1 * silk_2) / silk_1

# Result
a  # The amount of finished product (縑) in 斤


"""


The variable `a` will contain the answer in 斤.
"""


"""
Variable 'a' has wrong value. Expected: 65/2, Actual: 225/14"""
