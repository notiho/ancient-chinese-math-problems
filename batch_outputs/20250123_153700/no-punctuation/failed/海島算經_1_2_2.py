"""
今有南望方邑不知大小立兩表東西去六丈齊人目以索連之令東表與邑東南隅及東北隅參相直當東表之北卻行五步遙望邑西北隅入索東端二丈二尺六寸半又卻北行去表一十三步二尺遙望邑西北隅適與西表相參合問邑方及邑去表各幾何
術曰以入索乘後去表以兩表相去除之所得為景差以前去表減之不盡以為法置後去表以前去表減之餘以乘入索為實實如法而一得邑方求去表遠近者置後去表以景差減之餘以乘前去表為實實如法而一得邑去表
答曰邑方 a里 邑去表 b里 
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. The problem involves determining the size of a square city (邑方) and its distance from a reference point (邑去表) based on observations and measurements. Below is the translation of the procedure into Python code:


"""


"""
Suppose there is a square city to the south, the size of which is unknown. Two poles are erected 6 zhang apart, aligned east-west. 
Using a rope, the eastern pole is aligned with the southeast and northeast corners of the city. 
From the eastern pole, moving 5 bu northward, the western edge of the city is observed, and the rope is pulled inward by 2 zhang, 2 chi, 6 cun, and a half.
Then, moving 13 bu and 2 chi further north, the western edge of the city aligns perfectly with the western pole.

Question: What is the size of the square city (邑方), and how far is the city from the poles (邑去表)?

The procedure says:
1. Multiply the inward rope length (入索) by the second distance from the pole (後去表).
2. Divide the result by the distance between the two poles (兩表相去), obtaining the shadow difference (景差).
3. Subtract the first distance from the pole (前去表) from the shadow difference. If there is a remainder, use it as the divisor (法).
4. Multiply the inward rope length (入索) by the remainder to obtain the dividend (實). Divide the dividend by the divisor to obtain the size of the city (邑方).
5. To find the distance of the city from the poles (邑去表), subtract the shadow difference from the second distance from the pole (後去表). Multiply the remainder by the first distance from the pole (前去表). Divide the result by the divisor to obtain the distance.

Answer: The size of the city is *a* li, and the distance from the poles is *b* li.
"""

from fractions import Fraction

# Given data
兩表相去 = 6  # Distance between the two poles in zhang
前去表 = Fraction(5, 15)  # First distance from the pole in li (5 bu = 5/15 li)
後去表 = Fraction(13, 15) + Fraction(2, 300)  # Second distance from the pole in li (13 bu 2 chi = 13/15 + 2/300 li)
入索 = Fraction(2, 3) + Fraction(2, 30) + Fraction(6.5, 300)  # Inward rope length in li (2 zhang 2 chi 6.5 cun = 2/3 + 2/30 + 6.5/300 li)

# Step 1: Multiply 入索 by 後去表
step1 = 入索 * 後去表

# Step 2: Divide by 兩表相去 to get 景差
景差 = step1 / 兩表相去

# Step 3: Subtract 前去表 from 景差
remainder = 景差 - 前去表

# Step 4: Multiply 入索 by the remainder to get the dividend (實)
實 = 入索 * remainder

# Step 5: Divide 實 by the remainder to get the size of the city (邑方)
邑方 = 實 / remainder

# Step 6: To find the distance of the city from the poles (邑去表)
distance_remainder = 後去表 - 景差
實_distance = distance_remainder * 前去表
邑去表 = 實_distance / remainder

# Final results
a = 邑方
b = 邑去表

# Output the results
a, b


"""


### Explanation of Units:
1. **Bu (步)**: 1 bu = 1/15 li.
2. **Chi (尺)**: 1 chi = 1/10 bu = 1/150 li.
3. **Cun (寸)**: 1 cun = 1/10 chi = 1/1500 li.
4. **Zhang (丈)**: 1 zhang = 10 chi = 2/3 li.

### Notes:
- The calculations use fractions to ensure precision, as ancient Chinese mathematics often dealt with exact proportional reasoning.
- The final results `a` (邑方) and `b` (邑去表) are in li (ancient Chinese length unit).
"""


"""
Code error: both arguments should be Rational instances"""
