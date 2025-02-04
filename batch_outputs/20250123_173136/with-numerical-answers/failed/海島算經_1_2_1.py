"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a(=151/48)里 ；邑去表 b(=83/20)里 。
"""

"""
Suppose there is a square city visible to the south, but its size is unknown. Two poles are erected, one to the east and one to the west, 6 zhang apart. Aligning the observer's eye with the poles, a rope is stretched between them. The eastern pole is aligned with the southeast and northeast corners of the city. Moving 5 bu north from the eastern pole, the observer looks toward the northwest corner of the city, and the rope's eastern end is displaced inward by 2 zhang, 2 chi, 6 cun and a half. Moving further north, 13 bu and 2 chi from the eastern pole, the observer looks toward the northwest corner of the city, and the line aligns perfectly with the western pole. 

Question: What is the size of the square city and its distance from the poles?

The procedure says: Multiply the rope displacement by the second distance from the pole, and divide by the distance between the two poles. The result is the shadow difference. Subtract the first distance from the shadow difference. If there is a remainder, use it as the divisor. Place the second distance, subtract the first distance, and multiply the remainder by the rope displacement to obtain the dividend. Divide the dividend by the divisor to obtain the size of the city. 

To find the distance of the city from the poles: Place the second distance, subtract the shadow difference, and multiply the remainder by the first distance to obtain the dividend. Divide the dividend by the divisor to obtain the distance of the city from the poles.

Answer: The size of the city is *a*(=151/48) li, and the distance of the city from the poles is *b*(=83/20) li.
"""

# Constants
兩表相去 = 6  # 6 丈
入索 = Fraction(2 * 10 + 2, 10) + Fraction(6.5, 10)  # 2丈2尺6寸半 = 2.26丈
前去表 = Fraction(5, 15)  # 5步 = 5/15丈
後去表 = Fraction(13 * 15 + 2, 15)  # 13步2尺 = 13 2/15丈

# 以入索乘後去表，以兩表相去除之，所得為景差
景差 = (入索 * 後去表) / 兩表相去

# 以前去表減之，不盡以為法
法 = 景差 - 前去表

# 置後去表，以前去表減之，餘以乘入索為實
實_邑方 = (後去表 - 前去表) * 入索

# 實如法而一，得邑方
a = 實_邑方 / 法  # 151/48 里

# 求去表遠近者：置後去表，以景差減之，餘以乘前去表為實
實_去表 = (後去表 - 景差) * 前去表

# 實如法而一，得邑去表
b = 實_去表 / 法  # 83/20 里
"""
Code error: both arguments should be Rational instances"""
