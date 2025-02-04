"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose person A departs from Chang'an and takes 5 days to reach Qi. Person B departs from Qi and takes 7 days to reach Chang'an.
Now, person B departs 2 days earlier than person A. Question: after how many days will they meet?

Answer: they will meet after *a* days.
"""

# Define the speeds of A and B (distance per day)
# Let the total distance between Chang'an and Qi be 1 unit.
speed_A = Fraction(1, 5)  # A travels 1/5 of the distance per day
speed_B = Fraction(1, 7)  # B travels 1/7 of the distance per day

# Time difference: B departs 2 days earlier
time_difference = 2

# Distance B has already traveled in 2 days
distance_B_early = speed_B * time_difference

# Remaining distance between A and B when A starts
remaining_distance = 1 - distance_B_early

# Relative speed (combined speed of A and B moving toward each other)
relative_speed = speed_A + speed_B

# Time it takes for A and B to meet
a = remaining_distance / relative_speed

a#----- content ends here -----

"""
"""
