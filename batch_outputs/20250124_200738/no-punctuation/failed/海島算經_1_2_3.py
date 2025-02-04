"""
今有南望方邑不知大小立兩表東西去六丈齊人目以索連之令東表與邑東南隅及東北隅參相直當東表之北卻行五步遙望邑西北隅入索東端二丈二尺六寸半又卻北行去表一十三步二尺遙望邑西北隅適與西表相參合問邑方及邑去表各幾何
術曰以入索乘後去表以兩表相去除之所得為景差以前去表減之不盡以為法置後去表以前去表減之餘以乘入索為實實如法而一得邑方求去表遠近者置後去表以景差減之餘以乘前去表為實實如法而一得邑去表
答曰邑方 a里 邑去表 b里 
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. Let's translate the problem and solution into Python code step by step.

### Problem Description:
There is a square city (邑) to the south, whose size and distance are unknown. Two poles (表) are erected 6 zhang apart in the east-west direction. Using a rope (索), observations are made to determine the city's dimensions and distance.

1. From the east pole, the observer aligns the rope with the southeast and northeast corners of the city.
2. Moving 5 steps north from the east pole, the observer aligns the rope with the northwest corner of the city. The rope extends 2 zhang, 2 chi, 6 cun, and 5 fen (2丈2尺6寸半) beyond the east pole.
3. Moving further north, 13 steps and 2 chi from the east pole, the observer aligns the rope with the northwest corner of the city, and it aligns perfectly with the west pole.

The task is to calculate:
- The side length of the square city (邑方).
- The distance from the poles to the city (邑去表).

### Procedure:
1. **Calculate the shadow difference (景差):**
   - Multiply the rope extension (入索) by the second distance from the east pole (後去表).
   - Divide by the distance between the poles (兩表相去).
   - Subtract the first distance from the east pole (前去表) to get the shadow difference.

2. **Calculate the side length of the city (邑方):**
   - Use the shadow difference as the divisor (法).
   - Multiply the rope extension (入索) by the remainder of the second distance minus the first distance.
   - Divide by the shadow difference to get the side length.

3. **Calculate the distance to the city (邑去表):**
   - Subtract the shadow difference from the second distance.
   - Multiply the result by the first distance.
   - Divide by the shadow difference to get the distance to the city.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
兩表相去 = 6  # Distance between the poles in zhang
前去表 = 5  # First distance from the east pole in bu
後去表 = 13 + Fraction(2, 10)  # Second distance from the east pole in bu (13步2尺 = 13.2 bu)
入索 = 2 + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # Rope extension in zhang (2丈2尺6寸半)

# Step 1: Calculate 景差 (shadow difference)
景差 = Fraction(入索 * 後去表, 兩表相去) - 前去表

# Step 2: Calculate 邑方 (side length of the city)
法 = 景差
實 = 入索 * (後去表 - 前去表)
邑方 = Fraction(實, 法)

# Step 3: Calculate 邑去表 (distance to the city)
實_去表 = (後去表 - 景差) * 前去表
邑去表 = Fraction(實_去表, 法)

# Results
a = 邑方  # Side length of the city in zhang
b = 邑去表  # Distance to the city in zhang

# Output results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Conversion:**
   - All measurements are converted into consistent units (zhang, bu, chi, etc.) using fractions for precision.
   - For example, 2丈2尺6寸半 is converted into `2 + 2/10 + 6/100 + 5/1000` zhang.

2. **Shadow Difference (景差):**
   - The shadow difference is calculated using the formula provided in the procedure.

3. **City Side Length (邑方):**
   - The side length is calculated using the shadow difference as the divisor.

4. **Distance to the City (邑去表):**
   - The distance is calculated using the shadow difference and the distances from the poles.

### Final Answer:
- `a` is the side length of the city in zhang.
- `b` is the distance to the city in zhang.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -18573/17
Variable 'b' has wrong value. Expected: 83/20, Actual: -66085/17"""
