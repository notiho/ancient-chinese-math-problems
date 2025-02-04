"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a(=151/48)里 ；邑去表 b(=83/20)里 。
"""

#----- content starts here -----
"""
Suppose there is a square city visible to the south, but its size is unknown. Two poles are erected, 6 zhang apart, one to the east and one to the west. Aligning the eyes with the tops of the poles, a rope is stretched between them. The eastern pole is aligned with the southeast and northeast corners of the city. Moving 5 bu north of the eastern pole, the northwest corner of the city is observed, and the rope is found to be 2 zhang, 2 chi, 6 cun and a half inside the eastern pole. Moving further north, 13 bu and 2 chi from the eastern pole, the northwest corner of the city aligns with the western pole. 

Question: What is the size of the square city and its distance from the poles?

The procedure says:
- Multiply the rope's inward distance by the farther distance from the pole, and divide by the distance between the two poles. The result is the difference in shadow lengths. Subtract the nearer distance from the pole from this value. If there is a remainder, use it as the divisor.
- Place the farther distance from the pole, subtract the nearer distance from it, and multiply the remainder by the rope's inward distance. This is the dividend. Divide the dividend by the divisor to obtain the city's size.
- To find the city's distance from the poles:
  - Place the farther distance from the pole, subtract the shadow difference from it, and multiply the remainder by the nearer distance from the pole. This is the dividend. Divide the dividend by the divisor to obtain the city's distance from the poles.

Answer: The city's size is *a*(=151/48) li, and the city's distance from the poles is *b*(=83/20) li.
"""

# Constants
兩表相去 = 6  # 6 丈
前去表 = 5  # 5 步
後去表 = 13 + Fraction(2, 10)  # 13 步 2 尺
入索 = 2 + Fraction(2, 10) + Fraction(6.5, 100)  # 2 丈 2 尺 6 寸半

# Step 1: Calculate 景差 (shadow difference)
景差 = Fraction(入索 * 後去表, 兩表相去)

# Step 2: Calculate 法 (divisor for city size)
法 = 景差 - 前去表

# Step 3: Calculate 實 (dividend for city size)
實 = (後去表 - 前去表) * 入索

# Step 4: Calculate 邑方 (city size)
a = Fraction(實, 法)  # 151/48 里

# Step 5: Calculate 邑去表 (city distance from poles)
實_去表 = (後去表 - 景差) * 前去表
b = Fraction(實_去表, 法)  # 83/20 里#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
