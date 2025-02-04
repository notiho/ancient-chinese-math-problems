"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a rabbit starts running 100 steps ahead. A dog chases it for 250 steps but ends up 30 steps short of catching the rabbit. 
Question: if the dog does not stop, how many more steps does it need to take to catch the rabbit?

Answer: the dog needs to run *a* steps.
"""

# Rabbit's head start
兔先走 = 100

# Dog's chase
犬追 = 250

# Distance dog is short of catching the rabbit
犬差 = 30

# Relative speed: for every 1 step the rabbit takes, the dog gains (犬追 - 犬差) / 兔先走 steps
相對速度 = Fraction(犬追 - 犬差, 兔先走)

# Remaining distance to cover
剩餘距離 = 犬差

# Steps needed for the dog to catch the rabbit
a = 剩餘距離 / 相對速度

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 750/7, Actual: 150/11"""
