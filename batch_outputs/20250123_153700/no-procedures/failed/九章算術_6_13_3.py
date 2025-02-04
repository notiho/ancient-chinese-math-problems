"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
荅曰： a步 。
"""

"""
Suppose a rabbit starts running 100 steps ahead. A dog chases it for 250 steps but is still 30 steps behind the rabbit when it stops.
Question: If the dog does not stop, how many more steps does it need to catch the rabbit?

Answer: *a* steps.
"""

# Rabbit's head start
兔先走 = 100

# Dog's chase
犬追 = 250

# Distance remaining between the dog and the rabbit
距離差 = 30

# Rabbit's speed relative to the dog
# For every 1 step the rabbit takes, the dog takes 2.5 steps.
犬速 = Fraction(5, 2)  # Dog's speed
兔速 = 1  # Rabbit's speed

# Relative speed (dog's speed minus rabbit's speed)
相對速度 = 犬速 - 兔速

# Distance the dog needs to cover to catch the rabbit
需要追距離 = 距離差

# Time (in steps) it takes for the dog to catch the rabbit
時間 = Fraction(需要追距離, 相對速度)

# Distance the dog travels in that time
a = 犬速 * 時間

a  # This is the number of steps the dog needs to catch the rabbit.
"""
Variable 'a' has wrong value. Expected: 750/7, Actual: 50"""
