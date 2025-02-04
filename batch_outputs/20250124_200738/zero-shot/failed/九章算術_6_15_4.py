"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code and compute the value of the unknown "a" (the distance the owner's horse travels in one day). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
guest_horse_speed = 300  # Guest horse travels 300 li per day
time_guest_traveled = Fraction(1, 3)  # Guest traveled for 1/3 of a day
time_owner_traveled = Fraction(3, 4)  # Owner returned home after 3/4 of a day

# Step 1: Calculate the remaining time after the owner realized the guest forgot the clothes
remaining_time = time_owner_traveled - time_guest_traveled

# Step 2: Halve the remaining time to find the "法" (rule)
rule = remaining_time / 2

# Step 3: Multiply the rule by the guest's horse speed to find the owner's horse speed
a = rule * guest_horse_speed

# Output the result
a  # This is the owner's horse speed in li per day
#----- content ends here -----


"""


The variable `a` will contain the solution, which is the distance the owner's horse travels in one day.
"""


"""
Variable 'a' has wrong value. Expected: 780, Actual: 125/2"""
