"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the size of a square city ("邑方", represented as `a`) and the distance from the city to the observation point ("邑去表", represented as `b`).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
distance_between_poles = Fraction(6)  # 6 丈
rope_insertion_first = Fraction(2, 10) + Fraction(2, 100) + Fraction(6, 1000)  # 2丈2尺6寸半
steps_back_first = Fraction(5)  # 5 步
steps_back_second = Fraction(13) + Fraction(2, 10)  # 13步2尺

# Conversion factors
step_to_zhang = Fraction(6, 10)  # 1 步 = 6/10 丈
zhang_to_li = Fraction(1, 300)  # 1 丈 = 1/300 里

# Convert steps to 丈
steps_back_first_in_zhang = steps_back_first * step_to_zhang
steps_back_second_in_zhang = steps_back_second * step_to_zhang

# Calculate 景差 (difference in shadow lengths)
shadow_difference = (rope_insertion_first * steps_back_second_in_zhang) / distance_between_poles

# Calculate 邑方 (a)
a = (rope_insertion_first * (steps_back_second_in_zhang - steps_back_first_in_zhang)) / shadow_difference

# Calculate 邑去表 (b)
b = ((steps_back_second_in_zhang - shadow_difference) * steps_back_first_in_zhang) / shadow_difference

# Convert results to 里
a = a * zhang_to_li
b = b * zhang_to_li

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**:
   - The distance between the two poles is 6 丈.
   - The rope insertion for the first observation is 2 丈 2 尺 6 寸半, converted into a fraction.
   - The first observer steps back 5 步, and the second observer steps back 13 步 2 尺, both converted into 丈.

2. **Conversion Factors**:
   - 1 步 = 6/10 丈.
   - 1 丈 = 1/300 里.

3. **Calculations**:
   - The shadow difference (`景差`) is calculated using the formula provided in the problem.
   - The size of the square city (`邑方`, `a`) is calculated using the formula provided.
   - The distance from the city to the observation point (`邑去表`, `b`) is calculated using the formula provided.

4. **Units**:
   - The final results for `a` and `b` are converted into 里.

### Output:
The variables `a` and `b` will contain the size of the square city in 里 and the distance from the city to the observation point in 里, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: 41/3300
Variable 'b' has wrong value. Expected: 83/20, Actual: 2887/11300"""
