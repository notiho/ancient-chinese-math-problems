"""
今有鳧起南海，七日至北海；鴈起北海，九日至南海。今鳧鴈俱起。問︰何日相逢？
荅曰： a日 。
"""

#----- content starts here -----
"""
Suppose a wild duck (鳧) starts flying from the South Sea and takes 7 days to reach the North Sea.
A wild goose (鴈) starts flying from the North Sea and takes 9 days to reach the South Sea.
If both start flying at the same time, how many days will it take for them to meet?

Answer: *a* days.
"""

# Time taken by the duck to travel the entire distance
duck_time = 7

# Time taken by the goose to travel the entire distance
goose_time = 9

# The relative speed of the duck and the goose combined is 1/7 + 1/9 of the total distance per day
relative_speed = Fraction(1, duck_time) + Fraction(1, goose_time)

# The total distance is 1 (normalized to 1 unit)
total_distance = 1

# Time taken for them to meet is total distance divided by their relative speed
a = Fraction(total_distance, relative_speed)

# Result
a#----- content ends here -----

"""
"""
