"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This problem involves a complex geometric calculation based on ancient Chinese surveying techniques. Let's translate the procedure into Python code step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Given data
兩表相去 = 6  # 6 丈
前去表 = 5  # 5 步
後去表 = 13 + Fraction(2, 10)  # 13 步 2 尺 (1 步 = 10 尺)
入索 = 2 + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # 2 丈 2 尺 6 寸半 (1 丈 = 10 尺, 1 尺 = 10 寸)

# Step 1: Calculate 景差
景差 = Fraction(入索 * 後去表, 兩表相去)

# Step 2: Calculate 法
法 = 景差 - 前去表

# Step 3: Calculate 實 for 邑方
實_邑方 = (後去表 - 前去表) * 入索

# Step 4: Calculate 邑方
邑方 = Fraction(實_邑方, 法)

# Step 5: Calculate 實 for 邑去表
實_邑去表 = (後去表 - 景差) * 前去表

# Step 6: Calculate 邑去表
邑去表 = Fraction(實_邑去表, 法)

# Convert results to 里 (1 里 = 180 丈)
a = Fraction(邑方, 180)  # 邑方 in 里
b = Fraction(邑去表, 180)  # 邑去表 in 里

# Results
a, b
#----- content ends here -----


"""


### Explanation of the Code:
1. **景差 Calculation**: 景差 is calculated by multiplying `入索` with `後去表` and dividing by `兩表相去`.
2. **法 Calculation**: 法 is the difference between 景差 and 前去表.
3. **邑方 Calculation**: The formula for 邑方 uses the difference between 後去表 and 前去表, multiplied by 入索, and divided by 法.
4. **邑去表 Calculation**: The formula for 邑去表 uses the difference between 後去表 and 景差, multiplied by 前去表, and divided by 法.
5. **Conversion to 里**: Since the problem asks for the results in 里, we convert the results from 丈 to 里 (1 里 = 180 丈).

### Final Answer:
- 邑方 = `a` 里
- 邑去表 = `b` 里
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -6191/1020
Variable 'b' has wrong value. Expected: 83/20, Actual: -913/68"""
