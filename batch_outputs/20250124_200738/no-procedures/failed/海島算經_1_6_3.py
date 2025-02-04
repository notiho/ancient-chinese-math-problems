"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese mathematics problem involving geometry and similar triangles to calculate the depth of water. Let's break it down and solve it step by step.

---

### Problem Breakdown:
1. A right triangle is formed with the measuring tool (矩) on the bank.
2. The tool is used to measure the depth of the water by observing the reflection of the white stone at the bottom of the water.
3. The problem involves two setups:
   - In the first setup, the tool's height (句高) is 3 尺, and the lower leg (股) measurements are given.
   - In the second setup, the tool is raised by 4 尺, and new measurements are taken.
4. Using the principle of similar triangles, we calculate the depth of the water.

---

### Given Data:
- **First setup:**
  - 句高 = 3 尺
  - 股 (to water edge) = 4 尺 5 寸 = \( 4 + \frac{5}{10} = 4.5 \) 尺
  - 股 (to white stone) = 2 尺 4 寸 = \( 2 + \frac{4}{10} = 2.4 \) 尺

- **Second setup:**
  - 句高 = 3 尺 + 4 尺 = 7 尺
  - 股 (to water edge) = 4 尺
  - 股 (to white stone) = 2 尺 2 寸 = \( 2 + \frac{2}{10} = 2.2 \) 尺

---

### Solution:
We use the principle of similar triangles to calculate the depth of the water.

Let the depth of the water be \( a \) 丈 (1 丈 = 10 尺).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# First setup
句高_1 = 3  # 尺
股_水岸_1 = Fraction(4, 1) + Fraction(5, 10)  # 4 尺 5 寸 = 4.5 尺
股_白石_1 = Fraction(2, 1) + Fraction(4, 10)  # 2 尺 4 寸 = 2.4 尺

# Second setup
句高_2 = 3 + 4  # 句高 = 3 尺 + 4 尺 = 7 尺
股_水岸_2 = Fraction(4, 1)  # 4 尺
股_白石_2 = Fraction(2, 1) + Fraction(2, 10)  # 2 尺 2 寸 = 2.2 尺

# Using similar triangles, calculate the depth of the water (a 丈)
# Depth formula derived from similar triangles:
# a = (句高_1 * 股_白石_2 - 句高_2 * 股_白石_1) / (股_水岸_1 - 股_水岸_2)

numerator = (句高_1 * 股_白石_2) - (句高_2 * 股_白石_1)
denominator = 股_水岸_1 - 股_水岸_2
a = numerator / denominator

# Convert depth from 尺 to 丈 (1 丈 = 10 尺)
a_in_丈 = a / 10

# Output the result
a_in_丈
#----- content ends here -----


"""


---

### Explanation of the Formula:
The formula for the depth \( a \) is derived from the principle of similar triangles:
1. The ratio of the height of the tool to the distance to the white stone is the same as the ratio of the height difference to the distance to the water edge.
2. By setting up equations for the two setups and solving for \( a \), we derive the formula used in the code.

---

### Final Answer:
The depth of the water \( a \) is calculated in 丈 using the above Python code.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -102/5"""
