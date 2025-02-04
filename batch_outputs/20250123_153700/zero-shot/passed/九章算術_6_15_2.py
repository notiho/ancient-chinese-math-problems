"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the distance the owner's horse can travel in one day. Here's the Python code:


"""


from fractions import Fraction

# Given values
guest_horse_speed = 300  # in li per day
time_guest_traveled = Fraction(1, 3)  # 1/3 of a day
time_owner_traveled = Fraction(3, 4)  # 3/4 of a day

# Step 1: Calculate the remaining time after subtracting the guest's travel time
remaining_time = time_owner_traveled - time_guest_traveled

# Step 2: Halve the remaining time to find the "method" (法)
method = remaining_time / 2

# Step 3: Use the method to calculate the owner's horse speed
owner_horse_speed = (guest_horse_speed * (time_guest_traveled + method)) / method

# Solution
a = owner_horse_speed
a  # The owner's horse speed in li per day


"""


The variable `a` will contain the solution, which is the distance the owner's horse can travel in one day.
"""


"""
"""
