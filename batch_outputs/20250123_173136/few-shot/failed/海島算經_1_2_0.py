"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a complex geometric problem involving similar triangles and proportional reasoning. Let's translate the procedure into Python code step by step.

### Problem Description:
We are observing a square city (方邑) from a distance and trying to determine its side length (邑方) and the distance from the observation point to the city (邑去表). Two poles (表) are placed 6 zhang apart, and observations are made from different positions relative to these poles.

### Procedure:
1. Use the measurements of the rope (索) and distances walked to calculate the difference in shadow lengths (景差).
2. Use the difference in shadow lengths and the distances to calculate the side length of the city (邑方).
3. Use the same values to calculate the distance from the poles to the city (邑去表).

### Units:
- 1 丈 = 10 尺
- 1 里 = 300 丈

Now, let's implement the procedure in Python:


"""


from fractions import Fraction

# Given data
兩表相去 = 6  # Distance between the two poles in 丈
前去表 = 5  # Distance walked north from the east pole for the first observation in 步
入索 = Fraction(22, 10) + Fraction(6, 10) / 10  # Rope deviation in 丈 (2丈2尺6寸半)
後去表 = Fraction(13) + Fraction(2, 10)  # Distance walked north from the east pole for the second observation in 步

# Convert 步 to 丈 (1 步 = 6 尺 = 0.6 丈)
前去表 = 前去表 * Fraction(6, 10)
後去表 = 後去表 * Fraction(6, 10)

# Step 1: Calculate 景差
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate 邑方 (side length of the city)
法 = 後去表 - 前去表 - 景差
實 = (後去表 - 前去表) * 入索
邑方 = 實 / 法

# Step 3: Calculate 邑去表 (distance from the poles to the city)
實_去表 = (後去表 - 景差) * 前去表
邑去表 = 實_去表 / 法

# Convert results to 里 (1 里 = 300 丈)
邑方_里 = 邑方 / 300
邑去表_里 = 邑去表 / 300

# Final answers
a = 邑方_里
b = 邑去表_里

# Output results
a, b


"""


### Explanation of the Code:
1. **Input Conversion**: All distances are converted into consistent units (丈) for calculation.
2. **景差 Calculation**: This is the difference in shadow lengths based on the rope deviation and the second observation distance.
3. **邑方 Calculation**: Using the formula provided in the procedure, the side length of the city is calculated.
4. **邑去表 Calculation**: Using the same formula, the distance from the poles to the city is calculated.
5. **Unit Conversion**: The results are converted from 丈 to 里 for the final answer.

### Final Answer:
- 邑方 (side length of the city) = `a` 里
- 邑去表 (distance from the poles to the city) = `b` 里
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: 4633/242100
Variable 'b' has wrong value. Expected: 83/20, Actual: 2057/80700"""
