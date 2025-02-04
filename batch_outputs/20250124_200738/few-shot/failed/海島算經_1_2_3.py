"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This problem involves a geometric calculation based on observations and measurements. Let's translate the procedure into Python step by step:


"""

#----- content starts here -----

from fractions import Fraction

# Known values
兩表相去 = 6  # Distance between the two poles in 丈
入索 = Fraction(22, 10) + Fraction(6, 10) + Fraction(5, 10 * 10)  # 入索東端 (2丈2尺6寸半 converted to 丈)
前去表 = 5  # 前去表 distance in 步
後去表 = 13 + Fraction(2, 10)  # 後去表 distance in 步 (13步2尺 converted to 步)

# Step 1: Calculate 景差
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate 法
法 = 前去表 - 景差

# Step 3: Calculate 邑方 (area of the square city)
實_邑方 = (後去表 - 前去表) * 入索
邑方 = 實_邑方 / 法

# Step 4: Calculate 邑去表 (distance from the city to the poles)
實_邑去表 = (後去表 - 景差) * 前去表
邑去表 = 實_邑去表 / 法

# Convert results to 里 (1 里 = 180 步)
邑方_里 = 邑方 / (180 * 180)
邑去表_里 = 邑去表 / 180

# Final answers
a = 邑方_里
b = 邑去表_里

print(f"邑方: {a} 里")
print(f"邑去表: {b} 里")
#----- content ends here -----


"""


### Explanation of the Procedure:
1. **景差 Calculation**:
   - 景差 is calculated by multiplying the 入索 (the distance the rope enters) by the 後去表 (the distance of the second observation point from the pole) and dividing by the distance between the two poles.

2. **法 Calculation**:
   - 法 is obtained by subtracting 景差 from 前去表 (the distance of the first observation point from the pole).

3. **邑方 Calculation**:
   - The area of the square city (邑方) is calculated by multiplying the difference between 後去表 and 前去表 by 入索, then dividing by 法.

4. **邑去表 Calculation**:
   - The distance from the city to the poles (邑去表) is calculated by multiplying the difference between 後去表 and 景差 by 前去表, then dividing by 法.

5. **Conversion to 里**:
   - Since the problem asks for the results in 里, we convert the results from 步 to 里 using the conversion factor (1 里 = 180 步).

### Final Answer:
- The area of the city (邑方) is `a` 里².
- The distance from the city to the poles (邑去表) is `b` 里.
```
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -779/1371600
Variable 'b' has wrong value. Expected: 83/20, Actual: -77/508"""
