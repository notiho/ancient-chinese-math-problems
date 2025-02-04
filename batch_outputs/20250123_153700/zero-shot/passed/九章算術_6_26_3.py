"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
remaining_rice = 5  # in dou
outer_gate_tax = 3
middle_gate_tax = 5
inner_gate_tax = 7

# Compute the total rice initially held
# The formula is: 米 = (remaining_rice * outer_gate_tax * middle_gate_tax * inner_gate_tax) / ((outer_gate_tax - 1) * (middle_gate_tax - 1) * (inner_gate_tax - 1))
a = Fraction(remaining_rice * outer_gate_tax * middle_gate_tax * inner_gate_tax, 
             (outer_gate_tax - 1) * (middle_gate_tax - 1) * (inner_gate_tax - 1))

# The result
a  # in dou


"""


The variable `a` will hold the initial amount of rice in dou.
"""


"""
"""
