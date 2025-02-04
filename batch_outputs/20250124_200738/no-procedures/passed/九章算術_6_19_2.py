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

# Time for the duck to travel from South Sea to North Sea
duck_days = 7

# Time for the goose to travel from North Sea to South Sea
goose_days = 9

# The relative speed of the duck and goose combined (in terms of the distance covered per day)
relative_speed = Fraction(1, duck_days) + Fraction(1, goose_days)

# The total distance between the South Sea and North Sea is considered 1 unit.
# Time to meet is the reciprocal of the relative speed.
a = Fraction(1, relative_speed)#----- content ends here -----

"""
"""
