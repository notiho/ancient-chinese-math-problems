"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
答曰： a功 。
"""

"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang and 4 chi, the height is 3 zhang and 8 chi, and the length is 5550 chi. Each worker can complete 300 cubic chi of work in one day.
Question: how many worker-days (功) are required?

Answer: *a* worker-days.
"""

# Dimensions of the wall
上廣 = 2 * 10  # Convert zhang to chi
下廣 = 5 * 10 + 4  # Convert zhang to chi and add chi
高 = 3 * 10 + 8  # Convert zhang to chi and add chi
長 = 5550  # Already in chi

# Worker capacity per day
秋程人功 = 300  # chi^3 per worker per day

# Calculate the average width of the wall
平均廣 = Fraction(上廣 + 下廣, 2)

# Calculate the volume of the wall
體積 = 平均廣 * 高 * 長  # chi^3

# Calculate the total worker-days required
a = Fraction(體積, 秋程人功)  # worker-days

a
"""
"""
