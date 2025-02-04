"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
答曰： a功 。
"""

"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang 4 chi, the height is 3 zhang 8 chi, and the length is 5550 chi. Each worker can complete 300 cubic chi of work in one day.
Question: how many worker-days are required?

Answer: *a* worker-days.
"""

# Dimensions of the wall
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
下廣 = 5 * 10 + 4  # Convert zhang and chi to chi
高 = 3 * 10 + 8  # Convert zhang and chi to chi
長 = 5550  # Length in chi

# Worker efficiency
秋程人功 = 300  # Each worker completes 300 cubic chi per day

# Calculate the average width of the wall
平均廣 = Fraction(上廣 + 下廣, 2)

# Calculate the volume of the wall (V = average width * height * length)
體積 = 平均廣 * 高 * 長

# Calculate the total worker-days required (total volume / worker efficiency)
a = Fraction(體積, 秋程人功)

a
"""
"""
