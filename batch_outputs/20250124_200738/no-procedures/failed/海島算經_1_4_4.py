"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese mathematical problem involving geometry and the use of right triangles to calculate the height of a tower (樓高) based on observations from a mountain. Let's break it down and solve it step by step.

### Problem Breakdown:
1. A right triangle is formed on the mountain with:
   - The height of the mountain (句高) = 6 尺.
   - The base of the triangle (下股) = 1 丈 2 尺 = 12 尺.
   - The hypotenuse is the line of sight from the mountain to the base of the tower.

2. A second right triangle is formed with:
   - The base of the second triangle (上股) = 1 丈 1 尺 4 寸 = 11 尺 4 寸 = \( 11 + \frac{4}{10} = 11.4 \) 尺.
   - The distance between the two observation points = 3 丈 = 30 尺.

3. A small pole (小表) is placed at the intersection of the two lines of sight:
   - The height of the small pole = 8 寸 = \( \frac{8}{10} = 0.8 \) 尺.

4. The goal is to calculate the height of the tower (樓高).

---

### Solution:
We will use the properties of similar triangles and proportions to solve this step by step.

---


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = 6  # Mountain height in 尺
下股 = 12  # Lower base in 尺
上股 = Fraction(114, 10)  # Upper base in 尺 (11 尺 4 寸)
相去 = 30  # Distance between observation points in 尺
小表 = Fraction(8, 10)  # Height of the small pole in 尺

# Step 1: Calculate the height of the tower above the mountain (樓高 above mountain)
# Using similar triangles:
# (樓高 above mountain) / (小表) = (相去) / (上股 - 下股)
樓高_above_mountain = 小表 * 相去 / (上股 - 下股)

# Step 2: Add the mountain height to get the total height of the tower
樓高 = 樓高_above_mountain + 句高

# Convert to 丈 (1 丈 = 10 尺)
樓高_in_丈 = 樓高 / 10

# Answer
a = 樓高_in_丈
a
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1**: We calculate the height of the tower above the mountain using the property of similar triangles:
   \[
   \frac{\text{樓高 above mountain}}{\text{小表}} = \frac{\text{相去}}{\text{上股 - 下股}}
   \]
   Rearranging gives:
   \[
   \text{樓高 above mountain} = \text{小表} \times \frac{\text{相去}}{\text{上股 - 下股}}
   \]

2. **Step 2**: Add the height of the mountain (句高) to the height above the mountain to get the total height of the tower.

3. **Step 3**: Convert the result from 尺 to 丈 by dividing by 10.

---

### Final Answer:
The height of the tower is \( a \) 丈.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: -17/5"""
