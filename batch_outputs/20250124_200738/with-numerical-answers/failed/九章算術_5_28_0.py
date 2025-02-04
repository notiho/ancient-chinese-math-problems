"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a(=10063/50)尺 。用徒 b(=2600000/10063)人 。
"""

#----- content starts here -----
"""
Suppose there is a valley with an upper width of 2 zhang, a length of 7 zhang, a lower width of 8 chi, a length of 4 zhang, and a depth of 6 zhang and 5 chi.
Question: what is the total volume?

Answer: 52000 cubic chi.

Suppose the earth is transported back and forth over a distance of 200 bu, with an additional distance of 1 li for loading and unloading. The total journey is 58 li. Six people share one cart, and the cart carries 34 chi and 7 cun of earth.
Question: how much earth does each person transport, and how many workers are needed?

The procedure says: Multiply the volume of one cart by the total journey in bu to get the dividend.
Add the back-and-forth distance to the loading/unloading distance of 1 li, and multiply by the 6 people per cart to get the divisor.
Divide the dividend by the divisor to get the amount of earth transported by one person.
Divide the total volume by the amount transported by one person to get the number of workers required.

Answer: Each person transports *a*(=10063/50) cubic chi. The number of workers required is *b*(=2600000/10063).
"""

# 冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺
上廣 = 2 * 10  # Convert zhang to chi
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert zhang and chi to chi

# Calculate the average width and length
平均廣 = (上廣 + 下廣) / 2
平均袤 = (上袤 + 下袤) / 2

# Calculate the total volume
積 = 平均廣 * 平均袤 * 深  # 52000 cubic chi

# 載土往來二百步，載輸之間一里，程行五十八里，車載三十四尺七寸
往來步數 = 200
載輸之間 = 1 * 300  # Convert li to bu (1 li = 300 bu)
程行 = 58 * 300  # Convert li to bu
車載 = 34 + Fraction(7, 10)  # Convert chi and cun to chi
車人數 = 6

# 以一車積尺乘程行步數為實
實 = 車載 * 程行

# 置今往來步數，加載輸之間一里，以車六人乘之，為法
法 = (往來步數 + 載輸之間) * 車人數

# 除之，所得即一人所到尺
a = Fraction(實, 法)  # 10063/50 cubic chi

# 以所到約積尺，即用徒人數
b = Fraction(積 * 100, a)  # 2600000/10063 workers#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
