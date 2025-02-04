"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
To solve the problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves calculating the side length of a square city ("邑方", denoted as `a`) and the distance from the observation point to the city ("邑去表", denoted as `b`). The calculations involve proportions and the use of the given measurements.

Here is the Python code:


"""


from fractions import Fraction

# Given data
distance_between_poles = Fraction(6)  # 6 丈
first_retreat = Fraction(5)  # 5 步
second_retreat = Fraction(13) + Fraction(2, 10)  # 13 步 2 尺 (1 步 = 10 尺)
first_entry = Fraction(2) + Fraction(2, 10) + Fraction(6, 100)  # 2 丈 2 尺 6 寸半 (1 丈 = 10 尺, 1 尺 = 10 寸)

# Step 1: Calculate 景差 (difference in shadow lengths)
shadow_difference = (first_entry * second_retreat) / distance_between_poles - first_retreat

# Step 2: Calculate 邑方 (side length of the square city, a)
a = (first_entry * (second_retreat - first_retreat)) / shadow_difference

# Step 3: Calculate 邑去表 (distance from the observation point to the city, b)
b = (second_retreat - shadow_difference) * first_retreat / shadow_difference

# Results
a = a / 10  # Convert from 丈 to 里 (1 里 = 10 丈)
b = b / 10  # Convert from 丈 to 里 (1 里 = 10 丈)

# Output the results
a, b


"""


### Explanation of the Code:
1. **Input Data**: The problem provides measurements in 丈 (zhang), 步 (bu), 尺 (chi), and 寸 (cun). These are converted into fractions for precise calculations.
2. **Step 1**: Calculate the difference in shadow lengths (`景差`) using the formula provided in the problem.
3. **Step 2**: Calculate the side length of the square city (`邑方`, `a`) using the formula provided.
4. **Step 3**: Calculate the distance from the observation point to the city (`邑去表`, `b`) using the formula provided.
5. **Unit Conversion**: The results are converted from 丈 to 里 (1 里 = 10 丈).

The variables `a` and `b` contain the final results in 里.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -4633/70
Variable 'b' has wrong value. Expected: 83/20, Actual: -3307/14"""
