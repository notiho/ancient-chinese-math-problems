"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
術曰：置善行者一百步，減不善行者六十步，餘四十步，以為法。以善行者之一百步，乘不善行者先行一百步，為實。實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Define the speeds of the two walkers
speed_good = 100  # steps per unit time
speed_bad = 60    # steps per unit time

# Define the lead of the slower walker
lead = 100  # steps

# Calculate the time it takes for the faster walker to catch up
# Formula: time = lead / (speed_good - speed_bad)
time = Fraction(lead, speed_good - speed_bad)

# Calculate the number of steps the faster walker takes to catch up
# Formula: steps = speed_good * time
a = speed_good * time

# The result is stored in variable 'a'
a


"""


When you run this code, the variable `a` will contain the number of steps the faster walker takes to catch up.
"""


"""
"""
