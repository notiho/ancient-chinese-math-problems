"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the size of a square city (邑方, denoted as `a`) and the distance from the city to the observation posts (邑去表, denoted as `b`). The calculations involve geometric relationships and proportions.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
east_west_distance = Fraction(6)  # Distance between the two observation posts (6丈)
first_north_distance = Fraction(5)  # Distance moved north from the eastern post in the first observation (5步)
second_north_distance = Fraction(13) + Fraction(2, 10)  # Distance moved north from the eastern post in the second observation (13步2尺)
first_rope_in = Fraction(2) + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # Rope pulled in during the first observation (2丈2尺6寸半)

# Step 1: Calculate 景差 (difference in shadow lengths)
shadow_difference = (first_rope_in * second_north_distance) / east_west_distance

# Step 2: Calculate the size of the square city (邑方, a)
a = (first_rope_in * (second_north_distance - first_north_distance)) / shadow_difference

# Step 3: Calculate the distance from the city to the observation posts (邑去表, b)
b = (second_north_distance * (second_north_distance - shadow_difference)) / shadow_difference

# Output the results
a = a / 10  # Convert from 丈 to 里
b = b / 10  # Convert from 丈 to 里

a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The distances and measurements are converted into fractions to ensure precise calculations. The units are in 丈, 步, 尺, 寸, and converted as necessary.
2. **Shadow Difference (景差)**: This is calculated using the formula provided in the problem.
3. **Square City Size (邑方, `a`)**: The formula for the size of the city is applied using the given data.
4. **Distance to Observation Posts (邑去表, `b`)**: The formula for the distance is applied using the given data.
5. **Unit Conversion**: The final results are converted from 丈 to 里 (1里 = 10丈).

### Output:
The variables `a` and `b` will contain the size of the square city in 里 and the distance to the observation posts in 里, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: 41/110
Variable 'b' has wrong value. Expected: 83/20, Actual: 8217/3775"""
