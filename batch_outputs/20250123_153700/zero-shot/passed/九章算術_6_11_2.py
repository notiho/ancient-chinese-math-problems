"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
術曰：置善行者一百步，減不善行者六十步，餘四十步，以為法。以善行者之一百步，乘不善行者先行一百步，為實。實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Define the steps per unit time for the good and bad walkers
good_walker_steps = 100  # steps per unit time
bad_walker_steps = 60    # steps per unit time

# The bad walker starts 100 steps ahead
initial_lead = 100  # steps

# Calculate the relative speed difference
relative_speed = good_walker_steps - bad_walker_steps  # steps per unit time

# Calculate the time it takes for the good walker to catch up
# Time = Distance / Speed
time_to_catch_up = Fraction(initial_lead, relative_speed)  # unit time

# Calculate the number of steps the good walker takes to catch up
a = good_walker_steps * time_to_catch_up  # steps

a


"""


After running this code, the variable `a` will contain the number of steps the good walker takes to catch up.
"""


"""
"""
