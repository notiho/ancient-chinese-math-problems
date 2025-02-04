"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a guest's horse that travels 300 li per day. The guest forgets to bring their clothes, and after 1/3 of the day has passed, the host realizes it. The host takes the clothes, chases the guest, catches up, and returns home. By the time the host gets back home, 3/4 of the day has passed.

Question: How far does the host's horse travel in one day?

Answer: The host's horse travels *a* li.
"""

from fractions import Fraction

# Guest's horse speed
guest_speed = 300  # li per day

# Time passed before the host realizes
time_before_realizing = Fraction(1, 3)  # 1/3 of the day

# Time passed when the host returns home
time_when_returned = Fraction(3, 4)  # 3/4 of the day

# Time available for the host to chase and return
time_for_host = time_when_returned - time_before_realizing

# Distance traveled by the guest in 1/3 of the day
guest_distance = guest_speed * time_before_realizing

# Host's horse speed (assume it is faster than the guest's horse)
# Let the host's horse speed be x li per day. The host travels the same distance as the guest (to catch up) and then returns home.
# The host's total distance is 2 * guest_distance, and the time taken is time_for_host.
# Therefore, host_speed = total_distance / time_for_host.

host_speed = 2 * guest_distance / time_for_host

# Total distance traveled by the host's horse in one day
a = host_speed

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 480"""
