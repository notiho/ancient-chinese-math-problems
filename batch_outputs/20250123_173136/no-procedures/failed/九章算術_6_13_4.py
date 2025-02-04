"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
荅曰： a步 。
"""

"""
Suppose a rabbit starts running and is 100 steps ahead. A dog chases it and runs 250 steps but is still 30 steps behind the rabbit when it stops.
Question: If the dog does not stop, how many more steps does it need to catch the rabbit?

Answer: *a* steps.
"""

# Rabbit's head start
rabbit_head_start = 100

# Dog's steps
dog_steps = 250

# Distance remaining between the dog and the rabbit
remaining_distance = 30

# The relative speed of the dog compared to the rabbit
# For every 1 step the rabbit takes, the dog takes 2.5 steps.
relative_speed = 2.5 - 1  # Dog gains 1.5 steps per step the rabbit takes.

# Calculate how many steps the dog needs to catch the rabbit
a = Fraction(remaining_distance, relative_speed)

a
"""
Code error: both arguments should be Rational instances"""
