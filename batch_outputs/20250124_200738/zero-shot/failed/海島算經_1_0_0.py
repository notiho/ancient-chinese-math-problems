"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
table_height = Fraction(3)  # 表高 in 丈
distance_between_tables = Fraction(1000)  # 表間距離 in 步
front_table_retreat = Fraction(123)  # 前表卻行 in 步
back_table_retreat = Fraction(127)  # 後表卻行 in 步

# Calculations
# Island height (島高)
a = (table_height * distance_between_tables) / (back_table_retreat - front_table_retreat) + table_height

# Distance from the front table to the island (島去表數)
b = (front_table_retreat * distance_between_tables) / (back_table_retreat - front_table_retreat)

# Results
a  # 島高 in 丈
b  # 去表 in 步
#----- content ends here -----


"""


### Explanation:
1. **Island Height (a)**:
   - Multiply the table height by the distance between the tables.
   - Divide the result by the difference between the back table retreat and the front table retreat.
   - Add the table height to get the total island height.

2. **Distance to the Island (b)**:
   - Multiply the front table retreat by the distance between the tables.
   - Divide the result by the difference between the back table retreat and the front table retreat.

The variables `a` and `b` represent the island height and the distance from the front table to the island, respectively. Both are calculated using the given formulae.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 753
Variable 'b' has wrong value. Expected: 205/2, Actual: 30750"""
