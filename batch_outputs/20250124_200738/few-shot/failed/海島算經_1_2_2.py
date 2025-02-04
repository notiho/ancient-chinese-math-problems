"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. Let's translate the problem and the procedure into Python code step by step.

### Problem Description:
A square city is observed from a distance. Two poles are placed 6 zhang apart (east and west). A rope is used to align the observer's sight with specific corners of the city. Measurements are taken based on the observer's movement and the rope's alignment. The goal is to calculate the side length of the square city (`邑方`) and the distance from the poles to the city (`邑去表`).

### Procedure:
1. Use the rope's offset (`入索`) and the distances the observer moves (`前去表`, `後去表`) to calculate the difference in shadows (`景差`).
2. Use the shadow difference and the distances to calculate the side length of the city (`邑方`).
3. Use the shadow difference and distances to calculate the distance from the poles to the city (`邑去表`).

### Translation into Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
兩表相去 = 6  # Distance between the two poles in zhang
前去表 = 5  # Distance north from the east pole for the first observation in bu
後去表 = 13 + Fraction(2, 10)  # Distance north from the east pole for the second observation in bu
入索 = 2 + Fraction(2, 10) + Fraction(6, 100)  # Rope offset in zhang

# Step 1: Calculate 景差 (shadow difference)
景差 = Fraction(入索 * 後去表, 兩表相去)

# Step 2: Calculate 邑方 (side length of the square city)
法 = 後去表 - 前去表 - 景差
實 = 入索 * (後去表 - 前去表)
邑方 = Fraction(實, 法)

# Step 3: Calculate 邑去表 (distance from the poles to the city)
法 = 後去表 - 景差
實 = 前去表 * (後去表 - 景差)
邑去表 = Fraction(實, 法)

# Convert results to li (1 zhang = 1/15 li, 1 bu = 1/150 li)
邑方_里 = 邑方 * Fraction(1, 15)
邑去表_里 = 邑去表 * Fraction(1, 15)

# Final results
a = 邑方_里
b = 邑去表_里

# Output
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Conversion**: The given distances are converted into fractions for precise calculations.
2. **Shadow Difference (`景差`)**: Calculated using the rope offset (`入索`), the second observation distance (`後去表`), and the distance between the poles (`兩表相去`).
3. **City Side Length (`邑方`)**: Derived using the shadow difference, the distances (`前去表`, `後去表`), and the rope offset.
4. **Distance to City (`邑去表`)**: Calculated using the shadow difference and the distances.
5. **Unit Conversion**: Results are converted from zhang and bu to li for the final answer.

### Final Answer:
- `邑方 a里`: The side length of the square city in li.
- `邑去表 b里`: The distance from the poles to the city in li.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: 4633/12105
Variable 'b' has wrong value. Expected: 83/20, Actual: 1/3"""
