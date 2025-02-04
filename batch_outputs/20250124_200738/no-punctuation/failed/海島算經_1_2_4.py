"""
今有南望方邑不知大小立兩表東西去六丈齊人目以索連之令東表與邑東南隅及東北隅參相直當東表之北卻行五步遙望邑西北隅入索東端二丈二尺六寸半又卻北行去表一十三步二尺遙望邑西北隅適與西表相參合問邑方及邑去表各幾何
術曰以入索乘後去表以兩表相去除之所得為景差以前去表減之不盡以為法置後去表以前去表減之餘以乘入索為實實如法而一得邑方求去表遠近者置後去表以景差減之餘以乘前去表為實實如法而一得邑去表
答曰邑方 a里 邑去表 b里 
"""

#----- content starts here -----
This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. Let's carefully translate the procedure into Python code step by step.

"""
Suppose there is a square city visible to the south, but its size is unknown. Two poles are erected, 6 zhang apart, aligned east-west. 
Using a rope, the eastern pole is aligned with the southeast and northeast corners of the city. 
Standing north of the eastern pole, 5 bu away, the observer sees the northwest corner of the city, and the rope's eastern end is 2 zhang, 2 chi, 6 cun, and 5 fen (2.265 zhang) from the pole. 
Then, moving further north, 13 bu and 2 chi from the eastern pole, the observer sees the northwest corner of the city aligned with the western pole.

Question: What is the size of the square city (side length) and the distance from the poles to the city?

Procedure:
1. Multiply the rope's length (入索) by the second distance from the eastern pole (後去表).
2. Divide the result by the distance between the two poles (兩表相去) to get the shadow difference (景差).
3. Subtract the first distance from the eastern pole (前去表) from the shadow difference to get the remainder.
4. Use the remainder as the divisor (法).
5. Multiply the rope's length (入索) by the remainder to get the dividend (實).
6. Divide the dividend by the divisor to get the side length of the city (邑方).
7. To find the distance from the poles to the city:
   - Subtract the shadow difference from the second distance from the eastern pole (後去表).
   - Multiply the result by the first distance from the eastern pole (前去表) to get the dividend (實).
   - Divide the dividend by the divisor to get the distance from the poles to the city (邑去表).

Answer: The side length of the city is *a* li, and the distance from the poles to the city is *b* li.
"""

from fractions import Fraction

# Known values
兩表相去 = 6  # Distance between the two poles (6 zhang)
前去表 = Fraction(5, 15)  # First distance from the eastern pole (5 bu = 5/15 zhang)
後去表 = Fraction(13 * 15 + 2, 15)  # Second distance from the eastern pole (13 bu 2 chi = 13*15+2/15 zhang)
入索 = Fraction(2 * 10 + 2 + 6 / 10 + 5 / 100, 10)  # Rope length (2 zhang, 2 chi, 6 cun, 5 fen = 2.265 zhang)

# Step 1: Multiply the rope's length by the second distance from the eastern pole
step1 = 入索 * 後去表

# Step 2: Divide the result by the distance between the two poles to get the shadow difference
景差 = step1 / 兩表相去

# Step 3: Subtract the first distance from the shadow difference to get the remainder
remainder = 景差 - 前去表

# Step 4: Use the remainder as the divisor (法)
法 = remainder

# Step 5: Multiply the rope's length by the remainder to get the dividend (實)
實_邑方 = 入索 * remainder

# Step 6: Divide the dividend by the divisor to get the side length of the city (邑方)
邑方 = 實_邑方 / 法

# Step 7: To find the distance from the poles to the city:
# Subtract the shadow difference from the second distance from the eastern pole
step7 = 後去表 - 景差

# Multiply the result by the first distance from the eastern pole to get the dividend (實)
實_邑去表 = step7 * 前去表

# Divide the dividend by the divisor to get the distance from the poles to the city (邑去表)
邑去表 = 實_邑去表 / 法

# Convert results to li (1 zhang = 1/300 li)
a = 邑方 / 300  # Side length of the city in li
b = 邑去表 / 300  # Distance from the poles to the city in li

a, b  # Final results#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
