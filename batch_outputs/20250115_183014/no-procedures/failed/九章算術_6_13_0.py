"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
荅曰： a步 。
"""

"""
Suppose a rabbit starts running 100 steps ahead. A dog chases it for 250 steps but is still 30 steps behind when it stops.
Question: If the dog does not stop, how many more steps does it need to catch the rabbit?

Answer: *a* steps.
"""

# Rabbit's head start
rabbit_start = 100

# Dog's chase distance
dog_chase = 250

# Distance remaining between the dog and the rabbit
remaining_distance = 30

# The relative speed of the dog to the rabbit (dog covers 250 steps while the rabbit covers 100 steps)
relative_speed = Fraction(dog_chase, rabbit_start)

# The additional steps the dog needs to catch the rabbit
a = Fraction(remaining_distance, 1) * relative_speed

a
"""
Variable 'a' has wrong value. Expected: 750/7, Actual: 75"""
