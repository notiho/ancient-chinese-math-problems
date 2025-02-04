"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning to determine the size of a square city (邑) and its distance from a reference point (表). Let's break it down and translate it into Python code.

### Problem Breakdown:
- Two poles (表) are placed 6 丈 apart (1 丈 = 10 尺).
- Observations are made using a rope (索) to determine the alignment of the city corners.
- Measurements are taken at two positions north of the eastern pole:
  1. At 5 步 north, the rope enters the eastern pole by 2 丈 2 尺 6 寸 5 分 (converted to a single unit).
  2. At 13 步 2 尺 north, the city corner aligns with the western pole.
  
The goal is to calculate:
1. The side length of the square city (邑方).
2. The distance from the poles to the city (邑去表).

### Procedure:
1. **Calculate 景差 (difference in shadow lengths):**
   \[
   景差 = \frac{\text{入索} \times \text{後去表}}{\text{兩表相去}}
   \]
   Subtract 前去表 from 景差 to get 法.

2. **Calculate the city side length (邑方):**
   \[
   \text{邑方} = \frac{\text{入索} \times (\text{後去表} - \text{前去表})}{\text{法}}
   \]

3. **Calculate the distance to the city (邑去表):**
   \[
   \text{邑去表} = \frac{(\text{後去表} - \text{景差}) \times \text{前去表}}{\text{法}}
   \]

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Constants
兩表相去 = 6  # 6 丈
前去表 = 5  # 5 步
後去表 = 13 + Fraction(2, 10)  # 13 步 2 尺 (convert to 步)

# 入索 in 丈 (convert 2 丈 2 尺 6 寸 5 分 to 丈)
入索 = 2 + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)

# Step 1: Calculate 景差
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate 法
法 = 景差 - 前去表

# Step 3: Calculate 邑方 (city side length)
邑方 = (入索 * (後去表 - 前去表)) / 法

# Step 4: Calculate 邑去表 (distance to the city)
邑去表 = ((後去表 - 景差) * 前去表) / 法

# Convert results to 里 (1 里 = 180 丈)
邑方_里 = 邑方 / 180
邑去表_里 = 邑去表 / 180

# Output results
a = 邑方_里
b = 邑去表_里

print(f"邑方: {a} 里")
print(f"邑去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of Units:
1. **丈 (zhang):** A traditional Chinese unit of length, where 1 丈 = 10 尺.
2. **步 (bu):** Another unit of length, often used in ancient texts.
3. **里 (li):** A larger unit of length, where 1 里 = 180 丈.

### Final Answer:
- `a` represents the side length of the city in 里.
- `b` represents the distance from the poles to the city in 里.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -6191/1020
Variable 'b' has wrong value. Expected: 83/20, Actual: -913/68"""
