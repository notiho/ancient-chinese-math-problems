"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose a traveler's horse travels 300 li per day. The traveler forgets to bring their clothes, and after 1/3 of the day has passed, the host realizes it. The host then takes the clothes, chases the traveler, catches up, gives the clothes, and returns home. Upon returning home, 3/4 of the day has passed.

Question: How far does the host's horse travel in one day?

Answer: The host's horse travels *a* li.
"""

from fractions import Fraction

# Traveler's horse speed
traveler_speed = 300  # li/day

# Time before the host realizes (1/3 of a day)
time_before_realizing = Fraction(1, 3)

# Time remaining in the day after the host returns (3/4 of a day)
time_after_returning = Fraction(3, 4)

# Time taken by the host to complete the round trip
host_travel_time = time_after_returning - time_before_realizing

# Host's horse speed (same as the traveler's horse speed)
host_speed = traveler_speed

# Distance the host's horse travels in the round trip
round_trip_distance = host_speed * host_travel_time

# Since the host's horse travels to catch up and return, the one-way distance is half of the round trip
one_way_distance = round_trip_distance / 2

# The traveler has already traveled for 1/3 of the day
traveler_distance = traveler_speed * time_before_realizing

# The one-way distance the host travels must equal the distance the traveler has traveled
assert one_way_distance == traveler_distance

# Total distance the host's horse travels in one day
a = round_trip_distance

a  # Output the total distance traveled by the host's horse in one day (in li)#----- content ends here -----

"""
Code error: """
