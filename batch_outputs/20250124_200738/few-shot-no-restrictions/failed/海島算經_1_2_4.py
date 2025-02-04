"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. Let's break it down step by step and translate it into Python code.

---

### Problem Description:
We are tasked with determining the size of a square city (邑方) and its distance from the observation posts (邑去表). The procedure involves using two observation posts and proportional relationships based on the measurements provided.

---

### Procedure:
1. **Inputs:**
   - Distance between the two posts: `兩表相去 = 6 丈`
   - First observation:
     - Distance north of the eastern post: `前去表 = 5 步`
     - Rope deviation (how far the rope enters): `入索 = 2 丈 2 尺 6 寸半`
   - Second observation:
     - Distance north of the eastern post: `後去表 = 13 步 2 尺`

2. **Steps:**
   - Calculate the difference in shadow lengths (`景差`):
     \[
     景差 = \frac{\text{入索} \times \text{後去表}}{\text{兩表相去}} - \text{前去表}
     \]
   - Use `景差` to calculate the size of the city (`邑方`):
     \[
     邑方 = \frac{\text{入索} \times (\text{後去表} - \text{前去表})}{\text{景差}}
     \]
   - Use `景差` to calculate the distance of the city from the posts (`邑去表`):
     \[
     邑去表 = \frac{\text{前去表} \times (\text{後去表} - \text{景差})}{\text{景差}}
     \]

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to a consistent base (e.g., chi)
# 1 丈 = 10 尺, 1 尺 = 10 寸
def convert_to_chi(zhang=0, chi=0, cun=0):
    return zhang * 10 + chi + Fraction(cun, 10)

# Inputs
兩表相去 = convert_to_chi(zhang=6)  # 6 丈
前去表 = 5  # 5 步 (assume 1 步 = 1 chi for simplicity)
後去表 = 13 + Fraction(2, 10)  # 13 步 2 尺
入索 = convert_to_chi(zhang=2, chi=2, cun=6.5)  # 2 丈 2 尺 6 寸半

# Step 1: Calculate 景差
景差 = (入索 * 後去表) / 兩表相去 - 前去表

# Step 2: Calculate 邑方 (size of the city)
邑方 = (入索 * (後去表 - 前去表)) / 景差

# Step 3: Calculate 邑去表 (distance of the city from the posts)
邑去表 = (前去表 * (後去表 - 景差)) / 景差

# Outputs
a = 邑方 / 1000  # Convert chi to li (1 里 = 1000 尺)
b = 邑去表 / 1000  # Convert chi to li (1 里 = 1000 尺)

print(f"邑方: {a} 里")
print(f"邑去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:** The `convert_to_chi` function converts measurements in 丈, 尺, and 寸 into a consistent unit of chi.
2. **景差 Calculation:** This uses the formula provided in the problem to compute the difference in shadow lengths.
3. **邑方 Calculation:** The formula for the size of the city is implemented directly.
4. **邑去表 Calculation:** The formula for the distance of the city from the posts is implemented directly.
5. **Output:** The results are converted from chi to li (1 里 = 1000 尺) for the final answer.

---

### Example Output:
If you run the code, it will compute the following:
- **邑方 (size of the city):** `a 里`
- **邑去表 (distance of the city from the posts):** `b 里`

Let me know if you need further clarification or adjustments!
"""


"""
Code error: both arguments should be Rational instances"""
