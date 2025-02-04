"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese mathematical problem involving geometry and similar triangles. The problem describes a method of measuring the height of a tower (楼高) using a series of right triangles and proportions. Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. **First Triangle (偃矩山上):**
   - The height of the first triangle's vertical leg (句) is 6 尺.
   - The horizontal leg (股) extends 1 丈 2 尺 (12 尺).
   - The hypotenuse is used to sight the base of the tower.

2. **Second Triangle (重矩):**
   - The second triangle is set up 3 丈 (30 尺) further back.
   - From the hypotenuse of this triangle, the base of the tower is sighted again.
   - The horizontal leg (股) extends 1 丈 1 尺 4 寸 (11 尺 4 寸 = 11.4 尺).

3. **Small Triangle (小表):**
   - A small pole (小表) is placed at the intersection of the horizontal legs of the two triangles.
   - From the hypotenuse of the small triangle, the top of the tower is sighted.
   - The horizontal leg of the small triangle (股) is 8 寸 (0.8 尺).

4. **Goal:**
   - Calculate the height of the tower (楼高).

---

### Solution:
We will use the principle of similar triangles to solve this step by step.

---

### Step 1: Define the known values


---

### Step 2: Calculate the height of the tower
1. **First Triangle (偃矩山上):**
   - The ratio of height to horizontal leg is:
     \[
     \text{Ratio} = \frac{\text{句1}}{\text{股1}} = \frac{6}{12} = \frac{1}{2}
     \]

2. **Second Triangle (重矩):**
   - The total horizontal leg for the second triangle is:
     \[
     \text{Total 股2} = \text{股1} + \text{間距} = 12 + 30 = 42
     \]
   - Using the same ratio, the height of the second triangle is:
     \[
     \text{Height2} = \text{Total 股2} \times \text{Ratio} = 42 \times \frac{1}{2} = 21
     \]

3. **Small Triangle (小表):**
   - The height of the small triangle is proportional to its horizontal leg:
     \[
     \text{Height 小表} = \text{小表股} \times \text{Ratio} = 0.8 \times \frac{1}{2} = 0.4
     \]

4. **Tower Height (楼高):**
   - The total height of the tower is the sum of the height of the second triangle and the height of the small triangle:
     \[
     \text{楼高} = \text{Height2} + \text{Height 小表} = 21 + 0.4 = 21.4 \, \text{尺}
     \]
   - Convert 尺 to 丈 (1 丈 = 10 尺):
     \[
     \text{楼高} = \frac{21.4}{10} = 2.14 \, \text{丈}
     \]

---

### Final Answer:

"""

#----- content starts here -----

from fractions import Fraction

# Known values
句1 = 6  # First triangle's vertical leg (6 尺)
股1 = 12  # First triangle's horizontal leg (1 丈 2 尺 = 12 尺)

間距 = 30  # Distance between the two triangles (3 丈 = 30 尺)

股2 = Fraction(114, 10)  # Second triangle's horizontal leg (1 丈 1 尺 4 寸 = 11.4 尺)

小表股 = Fraction(8, 10)  # Small triangle's horizontal leg (8 寸 = 0.8 尺)

# Final height of the tower in 丈
a = Fraction(214, 100)  # 2.14 丈
print(f"楼高: {a} 丈")
#----- content ends here -----


"""


The height of the tower is **2 丈 1 尺 4 寸 (2.14 丈)**.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 107/50"""
