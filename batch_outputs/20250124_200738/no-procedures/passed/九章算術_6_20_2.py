"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose Person A departs from Chang'an and takes 5 days to reach Qi. Person B departs from Qi and takes 7 days to reach Chang'an.
Now, Person B departs 2 days earlier than Person A. 
Question: after how many days will they meet?

Answer: they will meet after *a* days.
"""

# Define the speeds of A and B (distance per day)
# Let the total distance between Chang'an and Qi be 1 unit
A_speed = Fraction(1, 5)  # A travels 1/5 of the distance per day
B_speed = Fraction(1, 7)  # B travels 1/7 of the distance per day

# Let the time elapsed after A starts be "a" days
# In that time, A travels A_speed * a, and B travels B_speed * (a + 2) (since B started 2 days earlier)

# The sum of their distances traveled must equal 1 (the total distance between Chang'an and Qi)
# A_speed * a + B_speed * (a + 2) = 1

# Solve for "a"
a = Fraction(1 - B_speed * 2, A_speed + B_speed)

# The answer is:
a#----- content ends here -----

"""
"""
