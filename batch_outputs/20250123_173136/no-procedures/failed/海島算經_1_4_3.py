"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese problem involving geometry and similar triangles. It calculates the height of a tower (楼高) based on measurements taken from a mountain using inclined lines and similar triangles.

Let's break it down step by step and solve it in Python.

---

### Problem Breakdown:
1. **Given:**
   - A mountain with a horizontal base (平地).
   - A measuring tool (偃矩) is placed on the mountain.
   - The height of the measuring tool's vertical leg (句) is 6 尺.
   - From the top of the vertical leg, an inclined line is drawn to the base of the tower (楼足), and the horizontal distance (入下股) is 1 丈 2 尺 (12 尺).
   - Another measuring tool is placed 3 丈 (30 尺) higher up the mountain.
   - From the top of this second tool, another inclined line is drawn to the base of the tower, and the horizontal distance (入上股) is 1 丈 1 尺 4 寸 (14 尺).
   - A small pole (小表) is placed at the intersection of the two inclined lines.
   - From the top of the vertical leg of the first tool, an inclined line is drawn to the top of the tower (楼岑端), and the horizontal distance (入小表) is 8 寸 (0.8 尺).

2. **Question:**
   - What is the height of the tower (楼高)?

---

### Solution:
We use the principle of similar triangles to calculate the height of the tower step by step.

---


"""


from fractions import Fraction

# Step 1: Define the given values
句高 = 6  # Height of the vertical leg (句) in 尺
入下股 = 12  # Horizontal distance to the base of the tower (入下股) in 尺
入上股 = 14  # Horizontal distance to the base of the tower from the second tool (入上股) in 尺
相去 = 30  # Distance between the two tools (相去) in 尺
入小表 = Fraction(8, 10)  # Horizontal distance to the small pole (入小表) in 尺

# Step 2: Calculate the height of the small pole (小表高)
# Using similar triangles:
# 小表高 / 入小表 = 句高 / 入下股
小表高 = 句高 * 入小表 / 入下股

# Step 3: Calculate the height of the tower (楼高)
# Using similar triangles again:
# (楼高 - 小表高) / 入上股 = (小表高 + 相去) / 入下股
楼高 = 小表高 + (小表高 + 相去) * 入上股 / 入下股

# Step 4: Convert the result to 丈
楼高_in_丈 = Fraction(楼高, 10)

# Output the result
楼高_in_丈


"""


---

### Explanation of the Code:
1. **Step 1:** Define the given values in terms of 尺 (chi). Convert smaller units like 寸 (cun) into 尺 where necessary.
2. **Step 2:** Use the first set of similar triangles to calculate the height of the small pole (小表高).
3. **Step 3:** Use the second set of similar triangles to calculate the total height of the tower (楼高).
4. **Step 4:** Convert the result from 尺 to 丈 (1 丈 = 10 尺).

---

### Final Answer:
The height of the tower (楼高) is `a` 丈, where `a` is the result of the calculation.
"""


"""
Missing variable in output: 'a'"""
