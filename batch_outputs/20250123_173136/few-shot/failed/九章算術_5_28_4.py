"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
Suppose there is a valley with the following dimensions:
- The upper width is 2 zhang, and the length is 7 zhang.
- The lower width is 8 chi, and the length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question 1: What is the total volume of the valley?
Answer: 52000 cubic chi.

Suppose:
- The round trip distance for transporting soil is 200 bu.
- The distance between the loading and unloading points is 1 li.
- The total journey is 58 li.
- 6 people share a cart, and the cart carries 34 chi and 7 cun of soil.

Question 2: How much soil does each person transport, and how many workers are needed in total?

The procedure says:
- Multiply the volume of one cart of soil by the total journey distance in bu to get the dividend.
- Add the round trip distance to the 1 li distance between loading and unloading points, and multiply this by the 6 people per cart to get the divisor.
- Divide the dividend by the divisor to get the amount of soil transported by one person.
- Divide the total soil volume by the amount transported by one person to get the total number of workers needed.

Answer: Each person transports *a* cubic chi. The total number of workers needed is *b*.
"""

from fractions import Fraction

# Question 1: Calculate the total volume of the valley
# Upper dimensions
上廣 = 2 * 10  # Convert zhang to chi
上袤 = 7 * 10  # Convert zhang to chi

# Lower dimensions
下廣 = 8  # Already in chi
下袤 = 4 * 10  # Convert zhang to chi

# Depth
深 = 6 * 10 + 5  # Convert zhang and chi to chi

# Volume formula for a frustum: V = (1/2) * 深 * (上面積 + 下面積)
上面積 = 上廣 * 上袤
下面積 = 下廣 * 下袤
積 = Fraction(1, 2) * 深 * (上面積 + 下面積)

# Total volume in cubic chi
積 = int(積)  # Convert to integer for simplicity
assert 積 == 52000  # Verify the given answer

# Question 2: Calculate the soil transported per person and the total workers needed
# Given data
載土往來步數 = 200  # Round trip distance in bu
載輸之間一里 = 300  # 1 li = 300 bu
程行 = 58 * 300  # Total journey distance in bu (58 li converted to bu)
車載積尺 = 34 + Fraction(7, 10)  # Cart capacity in cubic chi (34 chi 7 cun)
車人數 = 6  # Number of people sharing a cart

# Procedure
# Step 1: Calculate the dividend (volume transported by one cart over the total journey)
實 = 車載積尺 * 程行

# Step 2: Calculate the divisor (round trip distance + 1 li, multiplied by 6 people)
法 = (載土往來步數 + 載輸之間一里) * 車人數

# Step 3: Divide to find the soil transported by one person
人到積尺 = Fraction(實, 法)

# Step 4: Divide the total soil volume by the soil transported by one person to find the total workers needed
用徒人數 = Fraction(積, 人到積尺)

# Convert to integers for final answers
a = int(人到積尺)
b = int(用徒人數)

# Final answers
a, b
"""
Code error: """
