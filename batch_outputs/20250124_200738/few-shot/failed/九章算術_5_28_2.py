"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

#----- content starts here -----
"""
Suppose there is a valley with the following dimensions:
- The upper width is 2 zhang, and the upper length is 7 zhang.
- The lower width is 8 chi, and the lower length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: What is the total volume?

Answer: 52000 cubic chi.

Suppose the following conditions for transporting the soil:
- The round trip distance is 200 bu.
- The distance between the loading and unloading points is 1 li.
- The total journey is 58 li.
- 6 people share one cart.
- The cart carries 34 chi and 7 cun of soil.

Question: How much soil does one person transport, and how many workers are needed?

The procedure says:
- Multiply the volume of one cart by the total journey in bu to get the dividend.
- Add the round trip distance and the 1 li distance between loading and unloading points, and multiply this by the 6 people per cart to get the divisor.
- Divide the dividend by the divisor to get the amount of soil transported by one person.
- Divide the total soil volume by the amount transported by one person to get the number of workers needed.

Answer: One person transports *a* cubic chi. The number of workers needed is *b*.
"""

# 冥谷 dimensions
上廣 = 2 * 10  # Convert zhang to chi
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8  # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to chi

# Calculate the volume of the valley
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤
積 = (上積 + 下積) * 深 // 2  # Trapezoidal prism formula

# Verify the volume
assert 積 == 52000  # Given in the problem

# Transport conditions
往來步數 = 200
載輸之間 = 1 * 300  # Convert li to bu
程行 = 58 * 300  # Convert li to bu
車載 = 34 + Fraction(7, 10)  # Convert chi and cun to chi
車人數 = 6

# Calculate the soil transported by one person
實 = 車載 * 程行  # Dividend
法 = (往來步數 + 載輸之間) * 車人數  # Divisor
人到 = Fraction(實, 法)  # Soil transported by one person

# Calculate the number of workers needed
用徒 = Fraction(積, 人到)

# Final answers
a = 人到
b = 用徒

a, b#----- content ends here -----

"""
Code error: """
