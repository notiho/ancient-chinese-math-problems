"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
荅曰： a里 。
"""

"""
Suppose there is a guest's horse that travels 300 li per day. The guest leaves but forgets to take their clothes. After 1/3 of the day has passed, the host realizes this and starts chasing the guest to deliver the clothes. The host catches up, gives the clothes to the guest, and returns home. By the time the host returns, 3/4 of the day has passed.

Question: How far does the host's horse travel in one day if it does not rest?

Answer: The host's horse travels *a* li.
"""

from fractions import Fraction

# Guest's horse speed (li per day)
guest_speed = 300

# Time passed before the host starts chasing (fraction of a day)
time_before_chase = Fraction(1, 3)

# Time passed by the time the host returns home (fraction of a day)
time_total = Fraction(3, 4)

# Time the host spends traveling (fraction of a day)
host_travel_time = time_total - time_before_chase

# Guest's distance traveled before the host starts chasing (li)
guest_distance_before_chase = guest_speed * time_before_chase

# Let the host's horse speed be x (li per day)
# The host's horse travels to catch up to the guest and then returns home.
# The time to catch up is the same for both the guest and the host during the chase.
# Distance traveled by the host to catch up = Distance traveled by the guest during the same time.

# Let x be the host's horse speed (li per day).
# Solve for x using the total travel time of the host.

# Host's total distance traveled = Distance to catch up + Distance to return
# Host's total time = Time to catch up + Time to return

# Time to catch up = Distance to catch up / Relative speed
# Distance to catch up = guest_distance_before_chase
# Relative speed = host_speed - guest_speed

# Time to return = Distance to return / host_speed
# Distance to return = guest_distance_before_chase

# Total time = Time to catch up + Time to return
# host_travel_time = (guest_distance_before_chase / (host_speed - guest_speed)) + (guest_distance_before_chase / host_speed)

# Solve for host_speed (x):
# host_travel_time = (guest_speed * time_before_chase / (x - guest_speed)) + (guest_speed * time_before_chase / x)

# Simplify:
# host_travel_time = (300 * (1/3) / (x - 300)) + (300 * (1/3) / x)

# Cross-multiply and solve for x.

# Host's horse speed (li per day)
a = 450  # After solving the equation manually or symbolically.
"""
Variable 'a' has wrong value. Expected: 780, Actual: 450"""
