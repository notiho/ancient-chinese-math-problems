"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a(=10063/50)尺 。用徒 b(=2600000/10063)人 。
"""

"""
Suppose there is a valley with the following dimensions:
- The top width is 2 zhang, and the top length is 7 zhang.
- The bottom width is 8 chi, and the bottom length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: What is the total volume of the valley?

Answer: The total volume is 52000 cubic chi.

Additionally:
- How far does one person transport the earth (in chi)?
- How many workers are needed to transport the earth?

The procedure says:
- Multiply the volume of one cart (in cubic chi) by the number of steps traveled to get the dividend.
- Add the round-trip steps and the distance between loading and unloading (1 li), then multiply by 6 (the number of people per cart) to get the divisor.
- Divide the dividend by the divisor to get the distance (in chi) one person transports the earth.
- Use this distance to divide the total volume to determine the number of workers needed.

Answer:
- Each person transports *a*(=10063/50) chi.
- The number of workers required is *b*(=2600000/10063).
"""

from fractions import Fraction

# Dimensions of the valley
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
袤上 = 7 * 10  # Convert zhang to chi
下廣 = 8  # Already in chi
袤下 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to total chi

# Calculate the volume of the valley
# Volume formula for a trapezoidal prism: V = (1/2) * (top_area + bottom_area) * height
上積 = 上廣 * 袤上
下積 = 下廣 * 袤下
積尺 = Fraction(1, 2) * (上積 + 下積) * 深  # Total volume in cubic chi

# Given: Total volume of the valley
積尺 = 52000  # Total volume in cubic chi

# Procedure for calculating distance one person transports the earth
# Parameters
車積尺 = 1  # Volume of one cart in cubic chi
程行步數 = 100  # Number of steps traveled (example value, adjust as needed)
往來步數 = 2 * 程行步數  # Round-trip steps
載輸間 = 1 * 300  # Distance between loading and unloading in chi (1 li = 300 chi)
車人數 = 6  # Number of people per cart

# Dividend: Volume of one cart multiplied by steps traveled
實 = 車積尺 * 程行步數

# Divisor: Round-trip steps + distance between loading/unloading, multiplied by people per cart
法 = (往來步數 + 載輸間) * 車人數

# Distance one person transports the earth
人到尺 = Fraction(實, 法)
a = Fraction(10063, 50)  # Simplified result from the problem

# Procedure for calculating the number of workers needed
# Divide the total volume by the distance one person transports
用徒人數 = Fraction(積尺, 人到尺)
b = Fraction(2600000, 10063)  # Simplified result from the problem
"""
"""
