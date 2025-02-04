"""
今有望松生山上，不知高下。立兩表齊，高二丈，前後相去五十步，令後表與前表參相直。從前表卻行七步四尺，薄地遙望松末，與表端參合。又望松本，入表二尺八寸。复從後表卻行八步五尺，薄地遙望松末，亦與表端參合。問松高及山去表各幾何？
術曰：以入表乘表間為實。相多為法，除之。加入表，即得松高。求表去山遠近者：置表間，以前表卻行乘之為實。相多為法，除之，得山去表。
答曰：松高 a丈 ；山去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves determining the height of a tree ("松高") and the distance from the tree to the reference point ("山去表"). The calculations will be based on the given measurements and relationships.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
height_of_pole = Fraction(2)  # 2丈
distance_between_poles = Fraction(50)  # 50步
step1_distance = Fraction(7) + Fraction(4, 10)  # 7步4尺 = 7.4步
step1_offset = Fraction(2, 10) + Fraction(8, 100)  # 2尺8寸 = 0.28步
step2_distance = Fraction(8) + Fraction(5, 10)  # 8步5尺 = 8.5步

# Calculations for the height of the tree (松高)
numerator_height = step1_offset * distance_between_poles
denominator_height = step1_distance - step2_distance
a = numerator_height / denominator_height + height_of_pole

# Calculations for the distance from the tree to the reference point (山去表)
numerator_distance = distance_between_poles * step1_distance
denominator_distance = step1_distance - step2_distance
b = numerator_distance / denominator_distance

# Results
a  # 松高 in 丈
b  # 山去表 in 步
#----- content ends here -----


"""


### Explanation:
1. **Height of the tree (松高):**
   - The formula for the height of the tree is derived from the relationship between the offsets and distances.
   - `a = (入表 * 表間) / (前表卻行 - 後表卻行) + 表高`

2. **Distance from the tree to the reference point (山去表):**
   - The formula for the distance is derived from the relationship between the distances walked and the pole separation.
   - `b = (表間 * 前表卻行) / (前表卻行 - 後表卻行)`

3. **Units:**
   - The height of the tree (`a`) is in 丈.
   - The distance from the tree to the reference point (`b`) is in 步.

This code computes the values of `a` (tree height) and `b` (distance to the tree) using the given data and relationships.
"""


"""
Variable 'a' has wrong value. Expected: 307/25, Actual: -118/11
Variable 'b' has wrong value. Expected: 23/21, Actual: -3700/11"""
