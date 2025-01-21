"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the size of a square city (邑方, denoted as `a`) and the distance from the city to the observation posts (邑去表, denoted as `b`). The calculations involve using the given measurements and relationships.

Here is the Python code:


"""


from fractions import Fraction

# Given data
distance_between_posts = Fraction(6)  # 6 丈
first_observation_distance = Fraction(5)  # 5 步
second_observation_distance = Fraction(13) + Fraction(2, 10)  # 13 步 2 尺
rope_insertion_first = Fraction(2) + Fraction(2, 10) + Fraction(6, 100)  # 2 丈 2 尺 6 寸半

# Step 1: Calculate 景差 (difference in shadow lengths)
shadow_difference = (rope_insertion_first * second_observation_distance) / distance_between_posts

# Step 2: Calculate 邑方 (size of the square city, a)
numerator_a = rope_insertion_first * (second_observation_distance - first_observation_distance)
denominator_a = shadow_difference - first_observation_distance
a = numerator_a / denominator_a

# Step 3: Calculate 邑去表 (distance from the city to the posts, b)
numerator_b = first_observation_distance * (second_observation_distance - shadow_difference)
denominator_b = shadow_difference - first_observation_distance
b = numerator_b / denominator_b

# Results
a = a  # 邑方 in 丈²
b = b  # 邑去表 in 丈

# Output the results
a, b


"""


### Explanation of the Code:
1. **Input Data**: The problem provides measurements in 丈 (zhang), 步 (bu), 尺 (chi), and 寸 (cun). These are converted into fractions for precise calculations.
2. **Shadow Difference (景差)**: This is calculated using the formula provided in the problem.
3. **Square City Size (邑方, `a`)**: The formula for the size of the square city is derived from the problem's instructions.
4. **Distance to Posts (邑去表, `b`)**: The formula for the distance from the city to the posts is also derived from the problem's instructions.
5. **Results**: The results are stored in variables `a` (size of the city in 丈²) and `b` (distance to the posts in 丈).

This code computes the values of `a` and `b` as fractions, ensuring precision in the calculations.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -4633/7
Variable 'b' has wrong value. Expected: 83/20, Actual: -10285/7"""
