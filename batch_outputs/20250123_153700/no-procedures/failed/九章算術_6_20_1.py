"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
荅曰： a日 。
"""

"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi. 
Person B departs from Qi and takes 7 days to reach Chang'an. 
Now, person B departs 2 days earlier than person A. 
Question: after how many days will they meet?

Answer: *a* days.
"""

# Define the speeds of A and B (distance per day)
A_speed = Fraction(1, 5)  # A takes 5 days to cover the full distance
B_speed = Fraction(1, 7)  # B takes 7 days to cover the full distance

# The relative distance between A and B when A starts (B has already traveled for 2 days)
relative_distance = 2 * B_speed

# The combined speed of A and B moving toward each other
combined_speed = A_speed + B_speed

# Time (in days) for them to meet
a = relative_distance / combined_speed
"""
Variable 'a' has wrong value. Expected: 25/12, Actual: 5/6"""
