"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose a traveler's horse travels 300 li per day. The traveler forgets to bring their clothes, and after 1/3 of the day has passed, the host realizes it. 
The host takes the clothes, chases the traveler, catches up, gives the clothes, and returns home. 
By the time the host gets back home, 3/4 of the day has passed. 

Question: How far does the host's horse travel in one day?

Answer: The host's horse travels *a* li.
"""

from fractions import Fraction

# Traveler's horse speed
traveler_speed = 300  # li per day

# Time when the host realizes the traveler forgot their clothes
time_realized = Fraction(1, 3)  # 1/3 of the day

# Time when the host returns home
time_returned = Fraction(3, 4)  # 3/4 of the day

# Time the host spends traveling
host_travel_time = time_returned - time_realized  # (3/4 - 1/3) of the day

# Host's horse speed (assumed to be the same as the traveler's horse)
host_speed = traveler_speed  # li per day

# Total distance the host's horse travels
# The host travels to catch up with the traveler and then returns home
# The host's travel time is split equally between going and returning
host_distance = host_speed * host_travel_time * 2  # Multiply by 2 for round trip

# Final answer
a = host_distance
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 250"""
