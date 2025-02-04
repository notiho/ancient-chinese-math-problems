"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the size of a square city (邑方, denoted as `a`) and the distance from the city to the observation posts (邑去表, denoted as `b`). We will use the formulas provided in the problem description.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_between_posts = Fraction(6)  # 6 丈
first_observation_distance = Fraction(5)  # 5 步
second_observation_distance = Fraction(13, 1) + Fraction(2, 10)  # 13 步 2 尺
rope_displacement_first = Fraction(2, 1) + Fraction(2, 10) + Fraction(6, 100)  # 2 丈 2 尺 6 寸半

# Step 1: Calculate 景差 (difference in shadow lengths)
shadow_difference = (rope_displacement_first * second_observation_distance) / distance_between_posts - first_observation_distance

# Step 2: Calculate 邑方 (a)
numerator_a = rope_displacement_first * (second_observation_distance - first_observation_distance)
a = numerator_a / shadow_difference

# Step 3: Calculate 邑去表 (b)
numerator_b = first_observation_distance * (second_observation_distance - shadow_difference)
b = numerator_b / shadow_difference

# Results
a = a  # 邑方 in 丈²
b = b  # 邑去表 in 丈

# Output the results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**:
   - `distance_between_posts`: The distance between the two observation posts is 6 丈.
   - `first_observation_distance`: The distance from the first observation point to the post is 5 步.
   - `second_observation_distance`: The distance from the second observation point to the post is 13 步 2 尺 (converted to a fraction).
   - `rope_displacement_first`: The rope displacement at the first observation point is 2 丈 2 尺 6 寸半 (converted to a fraction).

2. **Formulas**:
   - 景差 (shadow difference) is calculated using the formula provided in the problem.
   - 邑方 (a) is calculated using the formula: `a = (rope_displacement_first * (second_observation_distance - first_observation_distance)) / shadow_difference`.
   - 邑去表 (b) is calculated using the formula: `b = (first_observation_distance * (second_observation_distance - shadow_difference)) / shadow_difference`.

3. **Units**:
   - All calculations are performed in 丈, 步, 尺, and 寸, converted to fractions for precision.

4. **Output**:
   - The results are stored in variables `a` (邑方) and `b` (邑去表).

Let me know if you need further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -4633/7
Variable 'b' has wrong value. Expected: 83/20, Actual: -16535/7"""
