"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the height of an island (denoted as `a`) and the distance from the island to the front pole (denoted as `b`). Here's the Python code:


"""


from fractions import Fraction

# Given data
table_height = Fraction(3)  # 表高 3 丈
table_distance = Fraction(1000)  # 表間距 1000 步
front_walk = Fraction(123)  # 前表卻行 123 步
back_walk = Fraction(127)  # 後表卻行 127 步

# Calculations
# Island height (a)
a = (table_height * table_distance) / (front_walk + back_walk) + table_height

# Distance from the front table to the island (b)
b = (front_walk * table_distance) / (front_walk + back_walk)

# Results
a  # Island height in 丈
b  # Distance from the front table to the island in 步


"""


This code computes the height of the island (`a`) and the distance from the front table to the island (`b`) using the formulas provided in the problem. The results are stored in the variables `a` and `b`, respectively, and are represented as fractions for precision.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 15
Variable 'b' has wrong value. Expected: 205/2, Actual: 492"""
