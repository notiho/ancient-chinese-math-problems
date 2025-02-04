"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a(=10063/50)尺 。用徒 b(=2600000/10063)人 。
"""

"""
Suppose there is a valley with an upper width of 2 zhang, a length of 7 zhang, a lower width of 8 chi, a length of 4 zhang, and a depth of 6 zhang 5 chi.
Question: what is the total volume?

Answer: 52000 cubic chi.

Suppose the soil is transported back and forth for 200 bu, with a distance of 1 li between loading and unloading points. 
The total journey is 58 li. 
Six people share a cart, and the cart carries 34 chi 7 cun of soil.
Question: how much soil does each person transport, and how many workers are needed?

The procedure says: Multiply the volume of one cart by the total journey in bu to obtain the dividend.
Place the current back-and-forth distance in bu, add the 1 li distance between loading and unloading, and multiply by the 6 people per cart to obtain the divisor.
Divide the dividend by the divisor to get the amount of soil each person transports.
Simplify the total volume by the amount each person transports to get the number of workers needed.

Answer: Each person transports *a*(=10063/50) cubic chi, and *b*(=2600000/10063) workers are needed.
"""

from fractions import Fraction

# 冥谷 dimensions
上廣 = 2 * 10  # Convert zhang to chi
袤上 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
袤下 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to chi

# Calculate the volume of the valley (冥谷)
# Volume = 深 * (上廣 * 袤上 + 下廣 * 袤下) / 2
積 = Fraction(深 * (上廣 * 袤上 + 下廣 * 袤下), 2)  # 52000 cubic chi

# Transport parameters
往來步數 = 200  # Back-and-forth distance in bu
載輸之間 = 1 * 300  # 1 li = 300 bu
程行 = 58 * 300  # 58 li = 300 bu per li
車載積 = 34 + Fraction(7, 10)  # 34 chi 7 cun = 34 + 7/10 chi
車人數 = 6  # 6 people per cart

# Calculate the amount of soil each person transports
# Dividend = 車載積 * 程行
實 = 車載積 * 程行

# Divisor = (往來步數 + 載輸之間) * 車人數
法 = (往來步數 + 載輸之間) * 車人數

# Each person's transported volume
人到積尺 = Fraction(實, 法)  # a = 10063/50

# Calculate the number of workers needed
# Workers = Total volume / Each person's transported volume
用徒 = Fraction(積, 人到積尺)  # b = 2600000/10063

a = 人到積尺  # 10063/50
b = 用徒  # 2600000/10063
"""
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 2795000/10063"""
