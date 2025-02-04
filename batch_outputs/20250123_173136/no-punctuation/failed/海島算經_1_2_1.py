"""
今有南望方邑不知大小立兩表東西去六丈齊人目以索連之令東表與邑東南隅及東北隅參相直當東表之北卻行五步遙望邑西北隅入索東端二丈二尺六寸半又卻北行去表一十三步二尺遙望邑西北隅適與西表相參合問邑方及邑去表各幾何
術曰以入索乘後去表以兩表相去除之所得為景差以前去表減之不盡以為法置後去表以前去表減之餘以乘入索為實實如法而一得邑方求去表遠近者置後去表以景差減之餘以乘前去表為實實如法而一得邑去表
答曰邑方 a里 邑去表 b里 
"""

This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. Let's translate the procedure into Python step by step.

"""
Suppose there is a square city to the south, whose size is unknown. Two poles are erected, 6 zhang apart, aligned east-west.
Using a rope, the observer aligns their sight such that the eastern pole, the southeast corner, and the northeast corner of the city are collinear.
The observer then moves 5 bu north of the eastern pole and observes the northwest corner of the city. The rope's eastern end is found to be 2 zhang, 2 chi, 6 cun and a half (2.265 zhang) away from the pole.
The observer then moves further north, 13 bu and 2 chi from the eastern pole, and observes the northwest corner of the city, aligning it with the western pole.

Question: What is the size of the square city (side length) and how far is the city from the poles?

The procedure says:
1. Multiply the rope's inward length by the second distance from the pole. Divide the result by the distance between the poles. The result is the difference in shadows (景差).
2. Subtract the first distance from the pole from the shadow difference. The remainder becomes the divisor.
3. Multiply the rope's inward length by the remainder to get the dividend. Divide the dividend by the divisor to get the side length of the city.
4. To find the distance from the poles to the city, subtract the shadow difference from the second distance from the pole. Multiply the remainder by the first distance from the pole to get the dividend. Divide the dividend by the divisor to get the distance.

Answer: The side length of the city is *a* li, and the distance from the poles to the city is *b* li.
"""

from fractions import Fraction

# Given values
兩表相去 = 6  # Distance between the two poles in zhang
前去表 = 5  # First distance from the eastern pole in bu
入索 = Fraction(2, 1) + Fraction(2, 10) + Fraction(6.5, 100)  # Rope's inward length in zhang (2 zhang, 2 chi, 6.5 cun)
後去表 = 13 + Fraction(2, 10)  # Second distance from the eastern pole in bu

# Convert bu to zhang (1 zhang = 10 bu)
前去表 = Fraction(前去表, 10)
後去表 = Fraction(後去表, 10)

# Step 1: Calculate 景差 (shadow difference)
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate the divisor for the city's side length
法 = 景差 - 前去表

# Step 3: Calculate the city's side length (邑方)
實 = 入索 * 法
邑方 = 實 / 法

# Step 4: Calculate the distance from the poles to the city (邑去表)
法_距離 = 後去表 - 景差
實_距離 = 前去表 * 法_距離
邑去表 = 實_距離 / 法_距離

# Convert results to li (1 zhang = 1/300 li)
a = 邑方 / 300
b = 邑去表 / 300

# Final results
a, b
"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
