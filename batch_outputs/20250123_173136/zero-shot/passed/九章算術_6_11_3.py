"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
術曰：置善行者一百步，減不善行者六十步，餘四十步，以為法。以善行者之一百步，乘不善行者先行一百步，為實。實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem in Python, we will translate the ancient Chinese math problem into code. Here's the solution:


"""


from fractions import Fraction

# Define the speeds of the two walkers
good_walker_speed = 100  # steps per unit time
bad_walker_speed = 60    # steps per unit time

# The bad walker has a head start of 100 steps
head_start = 100  # steps

# The difference in speed between the two walkers
speed_difference = good_walker_speed - bad_walker_speed  # steps per unit time

# Calculate the time it takes for the good walker to catch up
time_to_catch_up = Fraction(head_start, speed_difference)  # unit time

# Calculate the number of steps the good walker takes to catch up
a = good_walker_speed * time_to_catch_up  # steps

# The result
a


"""


When you run this code, the variable `a` will contain the number of steps the good walker takes to catch up.
"""


"""
"""
