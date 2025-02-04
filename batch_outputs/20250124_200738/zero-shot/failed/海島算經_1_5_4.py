"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
distance_between_poles = Fraction(9)  # 9丈
north_pole_to_first_position = Fraction(6)  # 6丈
rope_entry_north_end_first = Fraction(4, 10)  # 4丈2寸 = 4丈 + 2/10丈
rope_entry_pole_first = Fraction(12, 10)  # 1丈2尺 = 1丈 + 2/10丈
north_pole_to_second_position = Fraction(135, 10)  # 13丈5尺 = 13丈 + 5/10丈

# Step 1: Calculate the numerator (實)
numerator = (north_pole_to_second_position - north_pole_to_first_position) * rope_entry_pole_first

# Step 2: Calculate the denominator (法)
denominator = (north_pole_to_second_position * rope_entry_north_end_first) - (north_pole_to_first_position * distance_between_poles)

# Step 3: Calculate the width of the river (波口廣)
a = numerator / denominator

# The result is stored in variable `a`
a
#----- content ends here -----


"""


The variable `a` will contain the width of the river in 丈 (zhang).
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: -5/27"""
