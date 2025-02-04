"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi. Person B departs from Qi and takes 7 days to reach Chang'an.
Now, person B departs 2 days earlier than person A. 
Question: after how many days will they meet?

Answer: they will meet after *a* days.
"""

# Define the travel times
甲_至齊 = 5  # A takes 5 days to reach Qi
乙_至長安 = 7  # B takes 7 days to reach Chang'an

# Relative speeds (distance per day)
甲_速度 = Fraction(1, 甲_至齊)  # A's speed
乙_速度 = Fraction(1, 乙_至長安)  # B's speed

# B departs 2 days earlier, so B has a head start
乙_先行距離 = 乙_速度 * 2

# Combined speed (since they are moving toward each other)
相對速度 = 甲_速度 + 乙_速度

# Time until they meet
a = 乙_先行距離 / 相對速度

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/12, Actual: 5/6"""
