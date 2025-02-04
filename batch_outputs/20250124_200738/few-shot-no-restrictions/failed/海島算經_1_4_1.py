"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
This is a classic ancient Chinese geometry problem involving similar triangles and proportional reasoning. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
1. A person is standing on a mountain and observing a tower on flat ground.
2. A right triangle is formed with the mountain slope (hypotenuse), the height of the mountain (opposite side), and the horizontal distance (adjacent side).
3. The problem involves multiple observations with different setups:
   - First observation: The horizontal distance (lower base) is 1丈2尺 (12尺).
   - Second observation: A second triangle is set up 3丈 higher, and the horizontal distance (upper base) is 1丈1尺4寸 (11尺4寸).
   - Third observation: A small pole (小表) is placed at the intersection of the upper and lower bases, and the distance from the hypotenuse to the pole is 8寸.
4. The goal is to calculate the height of the tower (樓高).

### Procedure:
1. Subtract the upper base from the lower base to get the "difference" (法).
2. Multiply the difference by the height between the two triangles (矩閒, 3丈).
3. Divide the result by the lower base to get the intermediate height.
4. Multiply the intermediate height by the distance to the small pole (入小表, 8寸).
5. Divide the result by the difference (法) to get the height of the tower.

### Units:
- 1丈 = 10尺
- 1尺 = 10寸

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = 6  # Height of the mountain (句高) in 尺
下股 = 12  # Lower base (下股) in 尺
上股 = 11 + Fraction(4, 10)  # Upper base (上股) in 尺 (11尺4寸)
矩閒 = 3 * 10  # Distance between the two triangles (矩閒) in 尺 (3丈 = 30尺)
入小表 = Fraction(8, 10)  # Distance to the small pole (入小表) in 尺 (8寸)

# Step 1: Calculate the difference (法)
法 = 下股 - 上股

# Step 2: Multiply the difference by 矩閒
實1 = 法 * 矩閒

# Step 3: Divide by 下股 to get the intermediate height
中間高度 = Fraction(實1, 下股)

# Step 4: Multiply the intermediate height by 入小表
實2 = 中間高度 * 入小表

# Step 5: Divide by 法 to get the height of the tower
樓高 = Fraction(實2, 法)

# Convert the result to 丈
樓高_丈 = 樓高 / 10

# Output the result
a = 樓高_丈
print(f"樓高為 {a} 丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Units Conversion**: All measurements are converted to 尺 for consistency. The final result is converted back to 丈.
2. **Fractions**: The `Fraction` class is used to ensure precise calculations with non-integer values (e.g., 11尺4寸 and 8寸).
3. **Step-by-Step Calculation**: Each step of the procedure is implemented in the code, following the ancient method described in the problem.

### Final Answer:
The variable `a` contains the height of the tower in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 1/5"""
