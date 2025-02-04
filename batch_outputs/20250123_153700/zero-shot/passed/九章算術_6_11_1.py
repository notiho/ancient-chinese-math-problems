"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
術曰：置善行者一百步，減不善行者六十步，餘四十步，以為法。以善行者之一百步，乘不善行者先行一百步，為實。實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Define the speeds of the good walker and the bad walker
good_walker_speed = 100  # steps per unit time
bad_walker_speed = 60    # steps per unit time

# Define the lead of the bad walker
lead = 100  # steps

# Calculate the relative speed
relative_speed = good_walker_speed - bad_walker_speed  # steps per unit time

# Calculate the time it takes for the good walker to catch up
time_to_catch_up = Fraction(lead, relative_speed)  # unit time

# Calculate the distance the good walker travels to catch up
a = good_walker_speed * time_to_catch_up  # steps

# The answer is stored in variable 'a'
a


"""


When you run this code, the variable `a` will contain the number of steps the good walker needs to catch up to the bad walker.
"""


"""
"""
