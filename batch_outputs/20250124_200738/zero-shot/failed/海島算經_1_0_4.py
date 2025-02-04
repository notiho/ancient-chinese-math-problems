"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves using the heights of two poles (表), their distance apart, and the distances walked back from each pole to calculate the height of the island (島高) and the distance of the island from the poles (去表). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
pole_height = Fraction(3)  # 表高 = 3丈
distance_between_poles = Fraction(1000)  # 表間 = 1000步
front_pole_walk_back = Fraction(123)  # 前表卻行 = 123步
back_pole_walk_back = Fraction(127)  # 後表卻行 = 127步

# Calculating the height of the island (島高)
numerator_island_height = pole_height * distance_between_poles  # 表高乘表間為實
denominator_island_height = front_pole_walk_back + back_pole_walk_back  # 相多為法
island_height = numerator_island_height / denominator_island_height + pole_height  # 所得加表高，即得島高

# Calculating the distance from the front pole to the island (去表)
numerator_distance_to_island = front_pole_walk_back * distance_between_poles  # 前表卻行乘表間為實
denominator_distance_to_island = front_pole_walk_back + back_pole_walk_back  # 相多為法
distance_to_island = numerator_distance_to_island / denominator_distance_to_island  # 除之，得島去表數

# Assigning the results to variables
a = island_height  # 島高
b = distance_to_island  # 去表

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The height of the poles, the distance between them, and the distances walked back from each pole are given as inputs.
2. **Island Height Calculation**:
   - Multiply the pole height by the distance between the poles.
   - Divide this product by the sum of the distances walked back from each pole.
   - Add the pole height to this result to get the island height.
3. **Distance to Island Calculation**:
   - Multiply the distance walked back from the front pole by the distance between the poles.
   - Divide this product by the sum of the distances walked back from each pole to get the distance from the front pole to the island.
4. **Results**:
   - The height of the island is stored in variable `a`.
   - The distance from the front pole to the island is stored in variable `b`.

### Output:
The variables `a` and `b` will contain the height of the island and the distance to the island, respectively, in terms of fractions.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 15
Variable 'b' has wrong value. Expected: 205/2, Actual: 492"""
