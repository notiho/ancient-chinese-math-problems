"""
今有南望方邑不知大小立兩表東西去六丈齊人目以索連之令東表與邑東南隅及東北隅參相直當東表之北卻行五步遙望邑西北隅入索東端二丈二尺六寸半又卻北行去表一十三步二尺遙望邑西北隅適與西表相參合問邑方及邑去表各幾何
術曰以入索乘後去表以兩表相去除之所得為景差以前去表減之不盡以為法置後去表以前去表減之餘以乘入索為實實如法而一得邑方求去表遠近者置後去表以景差減之餘以乘前去表為實實如法而一得邑去表
答曰邑方 a里 邑去表 b里 
"""

"""
This is a complex ancient Chinese surveying problem involving geometry and proportional reasoning. Let's break it down step by step and encode the procedure into Python.

### Problem Explanation:
We are tasked with determining the side length of a square city (*邑方*) and its distance from the observation posts (*邑去表*). The procedure involves using measurements from two observation posts and applying proportional reasoning to calculate the unknowns.

### Procedure:
1. **Calculate the shadow difference (`景差`)**:
   - Multiply the "entered rope" (`入索`) by the distance of the second observation post from the first.
   - Divide the result by the distance between the two posts.
   - Subtract the first observation post's distance from the result to get the shadow difference.

2. **Calculate the side length of the city (`邑方`)**:
   - Use the shadow difference as the divisor.
   - Multiply the "entered rope" (`入索`) by the remainder of the second observation post's distance minus the first observation post's distance.
   - Divide the result by the shadow difference to get the side length of the city.

3. **Calculate the distance of the city from the posts (`邑去表`)**:
   - Subtract the shadow difference from the second observation post's distance.
   - Multiply the result by the first observation post's distance.
   - Divide the result by the shadow difference to get the distance of the city from the posts.

### Python Code:


"""


from fractions import Fraction

# Given data
兩表相去 = 6  # Distance between the two posts (in 丈)
前去表 = Fraction(5, 10)  # Distance of the first observation post (in 丈, converted from steps)
後去表 = Fraction(13, 10) + Fraction(2, 100)  # Distance of the second observation post (in 丈, converted from steps)
入索 = Fraction(2, 10) + Fraction(2, 100) + Fraction(6, 1000) + Fraction(5, 10000)  # Entered rope (in 丈)

# Step 1: Calculate 景差 (shadow difference)
景差 = (入索 * 後去表) / 兩表相去 - 前去表

# Step 2: Calculate 邑方 (side length of the city)
法 = 景差
實 = 入索 * (後去表 - 前去表)
邑方 = 實 / 法

# Step 3: Calculate 邑去表 (distance of the city from the posts)
法 = 景差
實 = (後去表 - 景差) * 前去表
邑去表 = 實 / 法

# Results
a = 邑方  # Side length of the city (in 丈)
b = 邑去表  # Distance of the city from the posts (in 丈)

# Convert results to 里 (1 里 = 300 丈)
a_in_里 = a / 300
b_in_里 = b / 300

# Final answer
print(f"邑方: {a_in_里} 里")
print(f"邑去表: {b_in_里} 里")


"""


### Explanation of Variables:
- `兩表相去`: Distance between the two posts (6 丈).
- `前去表`: Distance of the first observation post from the city (converted from steps to 丈).
- `後去表`: Distance of the second observation post from the city (converted from steps to 丈).
- `入索`: Length of the rope entering the city (converted from 丈, chi, and cun).
- `景差`: Shadow difference, calculated as described in the procedure.
- `邑方`: Side length of the city (in 丈, converted to 里 at the end).
- `邑去表`: Distance of the city from the posts (in 丈, converted to 里 at the end).

### Final Output:
The program will output the side length of the city (`邑方`) and the distance of the city from the posts (`邑去表`) in 里.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -18573/45017
Variable 'b' has wrong value. Expected: 83/20, Actual: -177017/90034"""
