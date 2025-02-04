"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a complex geometric problem involving similar triangles and proportional relationships. Let's translate the problem and procedure into Python code step by step.

### Problem Breakdown:
1. Two poles (east and west) are placed 6 zhang apart.
2. Observations are made from two positions north of the east pole:
   - At the first position, 5 bu north of the east pole, the western corner of the city aligns with the east pole and the string is offset by 2 zhang, 2 chi, 6 cun, and 5 fen.
   - At the second position, 13 bu and 2 chi north of the east pole, the western corner of the city aligns with the west pole.
3. The goal is to find:
   - The side length of the square city (*邑方*).
   - The distance from the poles to the city (*邑去表*).

### Procedure:
1. Calculate the difference in shadow lengths (*景差*).
2. Use the shadow difference and observations to calculate the side length of the city (*邑方*).
3. Use the shadow difference and observations to calculate the distance from the poles to the city (*邑去表*).

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
兩表相去 = 6  # Distance between the two poles (in zhang)

# Observations
前去表 = 5  # First observation distance north of the east pole (in bu)
後去表 = 13 + Fraction(2, 10)  # Second observation distance north of the east pole (in bu and chi)
入索 = 2 + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # String offset (in zhang, chi, cun, fen)

# Step 1: Calculate 景差 (shadow difference)
景差 = Fraction(入索 * 後去表, 兩表相去)

# Step 2: Calculate 邑方 (side length of the city)
法 = 後去表 - 前去表  # 法 is the difference between the two observation distances
實 = 入索 * 法  # 實 is the product of the string offset and 法
邑方 = Fraction(實, 景差 - 前去表)  # Calculate the side length of the city

# Step 3: Calculate 邑去表 (distance from the poles to the city)
實_去表 = 前去表 * (後去表 - 景差)  # Calculate the numerator for the distance
邑去表 = Fraction(實_去表, 法)  # Calculate the distance from the poles to the city

# Convert results to li (1 zhang = 1/15 li)
a = 邑方 / 15  # Convert side length to li
b = 邑去表 / 15  # Convert distance to li

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **景差 (Shadow Difference):**
   - Calculated by multiplying the string offset (*入索*) by the second observation distance (*後去表*) and dividing by the distance between the poles (*兩表相去*).

2. **邑方 (Side Length of the City):**
   - Calculated using the formula provided in the procedure:
     - Subtract the first observation distance (*前去表*) from the shadow difference (*景差*).
     - Use this as the divisor (*法*).
     - Multiply the string offset (*入索*) by the difference between the two observation distances (*後去表 - 前去表*) to get the numerator (*實*).
     - Divide the numerator by the divisor to get the side length.

3. **邑去表 (Distance to the City):**
   - Calculated using the formula provided in the procedure:
     - Subtract the shadow difference (*景差*) from the second observation distance (*後去表*).
     - Multiply this by the first observation distance (*前去表*) to get the numerator (*實_去表*).
     - Divide the numerator by the difference between the two observation distances (*法*) to get the distance.

4. **Conversion to li:**
   - Since 1 zhang = 1/15 li, the results are divided by 15 to convert from zhang to li.

### Final Answer:
- The side length of the city (*邑方*) is `a` li.
- The distance from the poles to the city (*邑去表*) is `b` li.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -6191/85
Variable 'b' has wrong value. Expected: 83/20, Actual: 2739/8200"""
