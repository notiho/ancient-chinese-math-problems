"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry to calculate the width of a river (波口廣). Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
1. Two poles (南表 and 北表) are placed 9 丈 apart (南北相去九丈).
2. A rope is stretched across the ground between the two poles.
3. Observations are made from different positions to determine the width of the river (波口廣).

The calculations involve geometric relationships, but the problem is complex and requires detailed trigonometric reasoning. Let's translate this into Python step by step.

---

### Python Code:


"""


from fractions import Fraction

# Constants
南北距離 = 9  # 南北相去九丈 (distance between the two poles in 丈)

# First observation:
北表西距離 = 6  # 去北表6丈
南岸入索北端 = Fraction(42, 10)  # 入索北端4丈2寸 (convert to 丈)

# Second observation:
北岸入表里 = Fraction(12, 10)  # 入表里1丈2尺 (convert to 丈)

# Third observation:
後退距離 = Fraction(135, 10)  # 卻後行13丈5尺 (convert to 丈)

# Using geometric relationships, calculate the width of the river (波口廣)
# The calculations involve proportional relationships and similar triangles.

# Step 1: Calculate the width of the river using the given observations
波口廣 = 南北距離 * 南岸入索北端 / (北表西距離 - 北岸入表里)

# Convert the result to li (里), where 1 里 = 300 丈
a = 波口廣 / 300

# Output the result
print(f"波口廣: {a} 里")


"""


---

### Explanation:
1. **南北距離**: The distance between the two poles is 9 丈.
2. **Observations**: The problem provides distances and offsets for observations made from different positions.
3. **Geometric Relationships**: The width of the river is calculated using proportional relationships derived from similar triangles.
4. **Conversion**: The final result is converted from 丈 to 里 (1 里 = 300 丈).

This code calculates the width of the river (波口廣) in 里.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 21/800"""
