"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi. Person B departs from Qi and takes 7 days to reach Chang'an.
Now, person B departs 2 days earlier than person A. 
Question: After how many days will they meet?

Answer: *a* days.
"""

# Define the speeds of A and B (distance per day)
A_speed = Fraction(1, 5)  # A travels 1/5 of the distance per day
B_speed = Fraction(1, 7)  # B travels 1/7 of the distance per day

# Relative distance covered by B in 2 days before A starts
B_early_distance = 2 * B_speed

# Combined speed of A and B moving toward each other
combined_speed = A_speed + B_speed

# Time (in days) for them to meet
a = B_early_distance / combined_speed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 25/12, Actual: 5/6"""
