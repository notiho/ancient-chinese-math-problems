"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the distance the owner's horse can travel in one day. We'll use the `Fraction` class to handle fractional calculations.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
guest_horse_speed = 300  # in li per day
time_guest_traveled = Fraction(1, 3)  # 1/3 of a day
time_owner_traveled = Fraction(3, 4)  # 3/4 of a day

# Step 1: Calculate the remaining time after the owner realized the guest forgot the clothes
remaining_time = time_owner_traveled - time_guest_traveled

# Step 2: Divide the remaining time by 2 (as the owner traveled to catch up and return)
time_to_catch_up = remaining_time / 2

# Step 3: Add the time_guest_traveled to the time_to_catch_up
total_time_owner_traveled = time_to_catch_up + time_guest_traveled

# Step 4: Calculate the owner's horse speed
# The owner's horse traveled the same distance as the guest's horse (300 li) in total_time_owner_traveled
a = guest_horse_speed / total_time_owner_traveled

# The result
a  # Owner's horse speed in li per day
#----- content ends here -----


"""


The variable `a` will contain the speed of the owner's horse in li per day.
"""


"""
Variable 'a' has wrong value. Expected: 780, Actual: 7200/13"""
