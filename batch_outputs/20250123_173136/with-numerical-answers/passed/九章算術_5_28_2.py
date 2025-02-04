"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a(=10063/50)尺 。用徒 b(=2600000/10063)人 。
"""

"""
Suppose there is a valley. At the top, its width is 2 zhang, and its length is 7 zhang.
At the bottom, its width is 8 chi, and its length is 4 zhang.
Its depth is 6 zhang and 5 chi.
Question: what is the total volume?

Answer: 52000 cubic chi.

Now, suppose the soil is transported back and forth for 200 bu, and the distance between the loading and unloading points is 1 li.
The total journey is 58 li. Six people share one cart, and the cart carries 34 chi and 7 cun of soil.
Question: how much soil does each person transport, and how many people are needed to move the total volume?

The procedure says: Multiply the volume of one cart by the total journey in bu to get the dividend.
Place the current round-trip distance in bu, add the 1 li of loading and unloading distance, and multiply by the 6 people per cart to get the divisor.
Divide the dividend by the divisor to get the amount of soil transported by one person.
Divide the total volume by the amount transported by one person to get the total number of people needed.

Answer: Each person transports *a*(=10063/50) cubic chi. The total number of people needed is *b*(=2600000/10063).
"""

from fractions import Fraction

# 冥谷 dimensions
上廣 = 2 * 10  # Convert zhang to chi
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8  # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to chi

# Calculate the volume of the valley
上積 = 上廣 * 上袤
下積 = 下廣 * 下袤
積 = Fraction((上積 + 下積) * 深, 2)  # Average of top and bottom areas multiplied by depth
積 = 52000  # Given in the problem

# Transportation details
往來步數 = 200  # Round-trip distance in bu
載輸之間 = 1 * 300  # Convert li to bu (1 li = 300 bu)
程行 = 58 * 300  # Convert li to bu
車載 = Fraction(34 * 10 + 7, 10)  # Convert chi and cun to chi
車人數 = 6  # Number of people per cart

# Calculate the amount of soil transported by one person
實 = 車載 * 程行  # Volume of one cart multiplied by total journey in bu
法 = (往來步數 + 載輸之間) * 車人數  # Round-trip distance + loading/unloading distance, multiplied by people per cart
人到 = Fraction(實, 法)  # Soil transported by one person

# Calculate the total number of people needed
用徒 = Fraction(積, 人到)  # Total volume divided by soil transported by one person

# Results
a = 人到  # Each person transports 10063/50 cubic chi
b = 用徒  # Total number of people needed is 2600000/10063
"""
"""
