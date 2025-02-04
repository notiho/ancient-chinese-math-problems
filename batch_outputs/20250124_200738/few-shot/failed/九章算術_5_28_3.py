"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

#----- content starts here -----
"""
Suppose there is a valley with an upper width of 2 zhang, a length of 7 zhang, a lower width of 8 chi, a length of 4 zhang, and a depth of 6 zhang and 5 chi.
Question: what is the total volume?

Answer: 52000 cubic chi.

Suppose the transportation involves 200 steps for a round trip, with a distance of 1 li between loading and unloading.
The total journey is 58 li, with 6 people sharing a cart that carries 34 chi and 7 cun of earth per trip.
Question: how much earth does each person transport, and how many people are required to move the total volume?

The procedure says: Multiply the volume of one cart by the total journey in steps to get the dividend.
Take the current round-trip steps, add the 1 li for loading and unloading, and multiply by 6 people to get the divisor.
Divide the dividend by the divisor to get the volume transported by one person.
Divide the total volume by the volume transported by one person to get the number of people required.

Answer: each person transports *a* cubic chi, and *b* people are required.
"""

from fractions import Fraction

# 冥谷 dimensions
上廣 = 2 * 10  # Convert zhang to chi
袤上 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
袤下 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to chi

# Calculate the volume of the valley
上積 = 上廣 * 袤上
下積 = 下廣 * 袤下
平均積 = Fraction(上積 + 下積, 2)
積尺 = 平均積 * 深

# Verify the total volume
assert 積尺 == 52000

# Transportation details
往來步數 = 200
載輸之間 = 1 * 300  # Convert li to steps (1 li = 300 steps)
程行 = 58 * 300  # Convert li to steps
車載積尺 = 34 + Fraction(7, 10)  # Convert chi and cun to chi
車人數 = 6

# Calculate the volume transported by one person
實 = 車載積尺 * 程行
法 = (往來步數 + 載輸之間) * 車人數
人到積尺 = Fraction(實, 法)

# Calculate the number of people required
用徒 = Fraction(積尺, 人到積尺)

# Final answers
a = 人到積尺
b = 用徒

a, b#----- content ends here -----

"""
Code error: """
