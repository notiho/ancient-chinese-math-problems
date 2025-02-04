"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem essentially describes a proportional relationship. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
silk_weight_1 = Fraction(14)  # 14斤
cloth_weight_1 = Fraction(10)  # 10斤
silk_weight_2 = Fraction(45) + Fraction(8, 16)  # 45斤8兩 (1斤 = 16兩)

# Calculation
a = (cloth_weight_1 * silk_weight_2) / silk_weight_1  # Proportional calculation

# Result
a  # Answer in 斤
#----- content ends here -----


"""


The variable `a` will contain the answer in 斤 (jin).
"""


"""
"""
