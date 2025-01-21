"""
今有築城，上廣二丈，下廣五丈四尺，高三丈八尺，長五千五百五十尺，秋程人功三百尺。問：須功幾何？
答曰： a功 。
"""

"""
Suppose there is a city wall to be built. The top width is 2 zhang, the bottom width is 5 zhang and 4 chi, the height is 3 zhang and 8 chi, and the length is 5550 chi. Each worker can complete 300 cubic chi of work in one day.
Question: how many worker-days are required?

Answer: *a* worker-days.
"""

# 上廣 (top width) = 2丈 = 20尺
上廣 = 20

# 下廣 (bottom width) = 5丈4尺 = 54尺
下廣 = 54

# 高 (height) = 3丈8尺 = 38尺
高 = 38

# 長 (length) = 5550尺
長 = 5550

# 秋程人功 (worker capacity per day) = 300尺³
人功 = 300

# Calculate the average width (average of top and bottom widths)
平均廣 = Fraction(上廣 + 下廣, 2)

# Calculate the total volume of the wall (average width * height * length)
總體積 = 平均廣 * 高 * 長

# Calculate the total worker-days required (total volume divided by worker capacity per day)
a = Fraction(總體積, 人功)

a
"""
"""
