"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the width of a river mouth ("波口廣") using geometric relationships and measurements. Here's the Python code:


"""


from fractions import Fraction

# Given data
north_south_distance = Fraction(9)  # Distance between the north and south poles (in 丈)
first_north_pole_offset = Fraction(6)  # First offset west of the north pole (in 丈)
first_north_pole_entry = Fraction(4, 10)  # First entry into the rope (in 丈, 4丈2寸 = 4.2丈)
first_south_pole_entry = Fraction(12, 10)  # First entry into the south pole (in 丈, 1丈2尺 = 1.2丈)
second_north_pole_offset = Fraction(135, 10)  # Second offset west of the north pole (in 丈, 13丈5尺 = 13.5丈)

# Step 1: Calculate the denominator (法)
denominator = (second_north_pole_offset * first_north_pole_entry) - (first_north_pole_offset * north_south_distance)

# Step 2: Calculate the numerator (實)
numerator = (second_north_pole_offset - first_north_pole_offset) * first_south_pole_entry

# Step 3: Calculate the width of the river mouth (波口廣)
a = numerator / denominator

# Output the result
a  # The width of the river mouth in 丈


"""


The variable `a` represents the width of the river mouth in 丈. This code uses the `Fraction` class to ensure precise calculations with fractions.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: -5/27"""
