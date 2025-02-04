"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and trigonometry to calculate the width of a river (波口廣). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. Two poles (表) are placed 9 丈 apart (南北相去九丈).
2. A rope is stretched across the ground (索薄地連之).
3. Observations are made from different positions to measure offsets and angles:
   - At 6 丈 west of the north pole, the rope is offset by 4 丈 2 寸 when looking at the south bank.
   - At the same position, the rope is offset by 1 丈 2 尺 when looking at the north bank.
   - At 13 丈 5 尺 west of the north pole, the rope aligns with the south pole when looking at the south bank.

The goal is to calculate the width of the river (波口廣).

---

### Assumptions:
1. 1 丈 = 10 尺, and 1 尺 = 10 寸.
2. The problem involves similar triangles and proportional relationships.

---

### Python Code:


"""


from fractions import Fraction

# Convert all measurements to 尺 for consistency
丈_to_尺 = 10
寸_to_尺 = Fraction(1, 10)

# Given data
南北距離 = 9 * 丈_to_尺  # 南北相去九丈
第一次觀測_北表西距 = 6 * 丈_to_尺  # 北表之西卻行六丈
第一次觀測_南岸偏移 = 4 * 丈_to_尺 + 2 * 寸_to_尺  # 入索北端四丈二寸
第一次觀測_北岸偏移 = 1 * 丈_to_尺 + 2  # 入表里一丈二尺

第二次觀測_北表西距 = 13 * 丈_to_尺 + 5  # 北表之西卻行十三丈五尺

# Step 1: Calculate the width of the river using similar triangles
# Using the first observation (南岸偏移 and 北岸偏移)
# Let 波口廣 = a (in 尺)
# From similar triangles:
# (波口廣 / 第一次觀測_南岸偏移) = (南北距離 / 第一次觀測_北岸偏移)

波口廣 = 南北距離 * 第一次觀測_南岸偏移 / 第一次觀測_北岸偏移

# Convert 波口廣 to 里 (1 里 = 300 丈 = 3000 尺)
波口廣_里 = 波口廣 / (300 * 丈_to_尺)

# Output the result
波口廣_里


"""


---

### Explanation of the Code:
1. All measurements are converted to 尺 for consistency.
2. The width of the river is calculated using the principle of similar triangles:
   - The ratio of the river's width to the south bank offset is equal to the ratio of the distance between the poles to the north bank offset.
3. Finally, the result is converted to 里 (1 里 = 300 丈 = 3000 尺).

---

### Final Answer:
The width of the river (波口廣) is `a` 里, where `a` is the result of the calculation above.
"""


"""
Missing variable in output: 'a'"""
