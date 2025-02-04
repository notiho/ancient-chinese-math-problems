"""
今有冥谷上廣二丈袤七丈下廣八尺袤四丈深六丈五尺問積幾何
荅曰五萬二千尺
載土往來二百步載輸之間一里程行五十八里六人共車車載三十四尺七寸問人到積尺及用徒各幾何
術曰以一車積尺乘程行步數為實置今往來步數加載輸之間一里以車六人乘之為法除之所得即一人所到尺以所到約積尺即用徒人數
荅曰人到 a尺 用徒 b人 
"""

#----- content starts here -----
"""
Suppose there is a valley with the following dimensions:
- The top width is 2 zhang, and the top length is 7 zhang.
- The bottom width is 8 chi, and the bottom length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question 1: What is the total volume of the valley?
Answer: 52000 cubic chi.

Additionally:
- The soil is transported back and forth over 200 bu.
- The distance between the loading and unloading points is 1 li.
- The total journey is 58 li.
- There are 6 people sharing one cart, and the cart carries 34 chi and 7 cun of soil.

Question 2: How much soil does each person transport, and how many people are needed to transport the total soil?

The procedure says:
- Multiply the soil carried by one cart by the total journey in bu to get the dividend.
- Add the back-and-forth bu and the 1 li distance between loading and unloading points, then multiply by 6 people per cart to get the divisor.
- Divide the dividend by the divisor to get the amount of soil transported by one person.
- Use the total soil volume and divide it by the amount transported by one person to determine the number of people required.

Answer: Each person transports *a* cubic chi, and *b* people are required.
"""

from fractions import Fraction

# Question 1: Calculate the total volume of the valley.

# Dimensions of the valley
上廣 = 2 * 10  # Convert zhang to chi
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang and 5 chi)

# Volume formula for a frustum: V = (1/2) * (top area + bottom area) * depth
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤
積 = Fraction(1, 2) * (上積 + 下積) * 深

# Total volume in cubic chi
total_volume = 積
assert total_volume == 52000  # Confirm the given answer

# Question 2: Calculate soil transported per person and the number of people required.

# Soil transported by one cart
車載 = 34 + Fraction(7, 10)  # Convert 34 chi and 7 cun to chi

# Total journey in bu
程行 = 58 * 300  # Convert li to bu (1 li = 300 bu)

# Dividend: soil carried by one cart multiplied by total journey
實 = 車載 * 程行

# Divisor: (back-and-forth bu + 1 li) * 6 people per cart
往來步數 = 200
載輸之間 = 1 * 300  # Convert li to bu
法 = (往來步數 + 載輸之間) * 6

# Soil transported by one person
人到 = Fraction(實, 法)

# Number of people required
用徒 = Fraction(total_volume, 人到)

# Simplify 用徒 to the nearest whole number (since people are discrete)
用徒 = 用徒.numerator // 用徒.denominator

# Final answers
a = 人到
b = 用徒#----- content ends here -----

"""
Code error: """
