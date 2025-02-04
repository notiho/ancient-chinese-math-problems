"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
guest_horse_speed = 300  # in li per day
time_guest_traveled = Fraction(1, 3)  # 1/3 of a day
time_owner_traveled = Fraction(3, 4)  # 3/4 of a day

# Step 1: Calculate the remaining time after the guest traveled 1/3 of a day
remaining_time = time_owner_traveled - time_guest_traveled

# Step 2: Halve the remaining time to find the effective time for the owner's horse
effective_time = remaining_time / 2

# Step 3: Add the time the guest traveled to the effective time
total_time = effective_time + time_guest_traveled

# Step 4: Multiply the total time by the guest horse's speed to find the owner's horse speed
a = total_time * guest_horse_speed

# The owner's horse speed in li per day
a
#----- content ends here -----


"""


The variable `a` will contain the solution, which is the distance the owner's horse can travel in one day.
"""


"""
Variable 'a' has wrong value. Expected: 780, Actual: 325/2"""
