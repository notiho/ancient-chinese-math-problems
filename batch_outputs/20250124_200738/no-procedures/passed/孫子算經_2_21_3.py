"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
答曰： a功 。
"""

#----- content starts here -----
"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. 
One person can complete 300 cubic chi of work in one day. 

Question: How many person-days of work are required?

Answer: *a* person-days.
"""

# Dimensions of the wall
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
下廣 = 5 * 10 + 4  # Convert zhang and chi to chi
高 = 3 * 10 + 8  # Convert zhang and chi to chi
長 = 5550  # Length in chi

# Average width of the wall (trapezoid formula)
平均廣 = Fraction(上廣 + 下廣, 2)

# Volume of the wall (in cubic chi)
體積 = 平均廣 * 高 * 長

# Work capacity per person per day
每日人功 = 300  # in cubic chi

# Total person-days required
a = Fraction(體積, 每日人功)

# Output the result
a#----- content ends here -----

"""
"""
