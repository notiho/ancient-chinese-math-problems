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

# Time taken by the duck (鳧) to travel from South Sea to North Sea
duck_time = 7

# Time taken by the goose (鴈) to travel from North Sea to South Sea
goose_time = 9

# The relative speed of the duck and goose is the sum of their speeds
# Speed of duck = 1/7 of the distance per day
# Speed of goose = 1/9 of the distance per day
relative_speed = Fraction(1, duck_time) + Fraction(1, goose_time)

# The total distance between the South Sea and the North Sea is 1 unit
# Time to meet = Distance / Relative Speed
a = Fraction(1, relative_speed)

# Result
a#----- content ends here -----

"""
"""
