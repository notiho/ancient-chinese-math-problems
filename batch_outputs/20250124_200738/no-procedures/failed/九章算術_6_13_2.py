"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a rabbit starts by running 100 steps ahead. A dog chases it for 250 steps but is still 30 steps behind the rabbit when it stops.
Question: If the dog does not stop, how many more steps does it need to catch the rabbit?

Answer: *a* steps.
"""

# Rabbit's step length and dog's step length
rabbit_step = 1  # Assume the rabbit's step length is 1 unit
dog_step = 2  # Assume the dog's step length is 2 units (dog is faster)

# Rabbit's head start
rabbit_head_start = 100 * rabbit_step

# Distance the dog has already traveled
dog_travel = 250 * dog_step

# Remaining gap between the dog and the rabbit
remaining_gap = rabbit_head_start - dog_travel + 30 * rabbit_step

# Relative speed difference between the dog and the rabbit
relative_speed = dog_step - rabbit_step

# Additional steps the dog needs to catch the rabbit
a = Fraction(remaining_gap, relative_speed)
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 750/7, Actual: -370"""
