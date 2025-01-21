"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a complex geometric problem involving similar triangles and proportional reasoning. Let's carefully translate the procedure into Python code step by step.

### Problem Description
We are tasked with determining the side length of a square city (`邑方`) and the distance from the observation point to the city (`邑去表`). The procedure involves using measurements of the offsets of a rope and distances between observation points to calculate these values.

### Procedure Breakdown
1. **景差 (Shadow Difference):**  
   Multiply the rope offset (`入索`) by the second observation distance (`後去表`), then divide by the distance between the two poles (`兩表相去`). Subtract the first observation distance (`前去表`) from the result to get the shadow difference. If there is a remainder, it becomes the divisor (`法`).

2. **邑方 (City Side Length):**  
   Subtract the first observation distance (`前去表`) from the second observation distance (`後去表`). Multiply the result by the rope offset (`入索`) to get the dividend (`實`). Divide the dividend by the divisor (`法`) to get the side length of the city.

3. **邑去表 (Distance to City):**  
   Subtract the shadow difference (`景差`) from the second observation distance (`後去表`). Multiply the result by the first observation distance (`前去表`) to get the dividend (`實`). Divide the dividend by the divisor (`法`) to get the distance to the city.

### Python Code Implementation


"""


from fractions import Fraction

# Given data
兩表相去 = 6  # Distance between the two poles in 丈
前去表 = 5  # First observation distance in 步
後去表 = 13 + Fraction(2, 10)  # Second observation distance in 步 (13步2尺 = 13.2步)
入索 = 2 + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # Rope offset in 丈 (2丈2尺6寸半 = 2.265丈)

# Step 1: Calculate 景差 (Shadow Difference)
景差 = Fraction(入索 * 後去表, 兩表相去) - 前去表

# Step 2: Calculate 法 (Divisor)
法 = 景差 if 景差.denominator == 1 else 景差

# Step 3: Calculate 邑方 (City Side Length)
邑方_實 = (後去表 - 前去表) * 入索
邑方 = Fraction(邑方_實, 法)

# Step 4: Calculate 邑去表 (Distance to City)
邑去表_實 = (後去表 - 景差) * 前去表
邑去表 = Fraction(邑去表_實, 法)

# Final results
a = 邑方  # City side length in 丈
b = 邑去表  # Distance to city in 丈

# Convert results to 里 (1 里 = 300 丈)
a_in_里 = a / 300
b_in_里 = b / 300

print(f"邑方: {a_in_里} 里")
print(f"邑去表: {b_in_里} 里")


"""


### Explanation of Units
- **丈 (zhang):** A traditional Chinese unit of length.
- **步 (bu):** Another traditional unit of length, often used in measurements.
- **里 (li):** A larger unit of length, where 1 里 = 300 丈.

### Final Answer
- `邑方 a里`: The side length of the city in 里.
- `邑去表 b里`: The distance from the observation point to the city in 里.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -18573/17
Variable 'b' has wrong value. Expected: 83/20, Actual: -66085/17"""
