"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
guest_horse_speed = 300  # in li per day
time_guest_traveled = Fraction(1, 3)  # 1/3 of the day
time_owner_traveled = Fraction(3, 4)  # 3/4 of the day

# Step 1: Calculate the difference in time
time_difference = time_owner_traveled - time_guest_traveled

# Step 2: Half the time difference
half_time_difference = time_difference / 2

# Step 3: Add the time_guest_traveled to half_time_difference
effective_time = time_guest_traveled + half_time_difference

# Step 4: Multiply the effective time by the guest horse speed
a = effective_time * guest_horse_speed

# The result is stored in variable 'a'
a  # This is the speed of the owner's horse in li per day


"""


The variable `a` will contain the speed of the owner's horse in li per day.
"""


"""
Variable 'a' has wrong value. Expected: 780, Actual: 325/2"""
