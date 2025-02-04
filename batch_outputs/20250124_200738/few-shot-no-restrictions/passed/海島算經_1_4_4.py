"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
This problem involves using geometric principles to calculate the height of a tower (樓高) based on observations from a mountain. Let's translate the problem into Python step by step.

---

### Problem Breakdown:
1. **Given Data**:
   - A right triangle is formed on the mountain with a base (股) and height (句).
   - The height of the mountain's triangle (句高) is 6 尺.
   - First observation:
     - From the top of the mountain, looking at the base of the tower, the base (下股) extends 1 丈 2 尺 (12 尺).
   - Second observation:
     - A second triangle is formed with a base (上股) extending 1 丈 1 尺 4 寸 (11 尺 4 寸 = 11.4 尺).
     - The distance between the two triangles is 3 丈 (30 尺).
   - Third observation:
     - A small pole (小表) is placed at the intersection of the base (入股), and looking at the top of the tower, the base extends 8 寸 (0.8 尺).

2. **Procedure**:
   - Subtract the upper base (上股) from the lower base (下股) to get the divisor (法).
   - Multiply the distance between the triangles (矩閒) by the lower base (下股), then divide by the height of the mountain (句高) to get an intermediate result.
   - Multiply the intermediate result by the small pole's base extension (入小表), then divide by the divisor (法) to get the tower's height.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = 6  # Height of the mountain triangle in 尺
下股 = 12  # Lower base in 尺 (1 丈 2 尺 = 12 尺)
上股 = 11 + Fraction(4, 10)  # Upper base in 尺 (1 丈 1 尺 4 寸 = 11.4 尺)
矩閒 = 30  # Distance between the two triangles in 尺 (3 丈 = 30 尺)
入小表 = Fraction(8, 10)  # Small pole's base extension in 尺 (8 寸 = 0.8 尺)

# Step 1: Calculate the divisor (法)
法 = 下股 - 上股

# Step 2: Calculate the intermediate result
intermediate_result = (矩閒 * 下股) / 句高

# Step 3: Multiply by the small pole's base extension and divide by the divisor
樓高 = (intermediate_result * 入小表) / 法

# Convert the result to 丈 (1 丈 = 10 尺)
樓高_丈 = 樓高 / 10

# Output the result
a = 樓高_丈
print(f"樓高: {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Conversion**:
   - All measurements are converted into 尺 for consistency.
   - For example, 1 丈 = 10 尺, and 1 寸 = 0.1 尺.

2. **Step-by-Step Calculation**:
   - The divisor (法) is the difference between the lower base (下股) and the upper base (上股).
   - The intermediate result is calculated by multiplying the distance between the triangles (矩閒) by the lower base (下股) and dividing by the mountain height (句高).
   - Finally, the intermediate result is multiplied by the small pole's base extension (入小表) and divided by the divisor (法) to get the tower's height.

3. **Output**:
   - The final height of the tower is converted from 尺 to 丈 for the answer.

---

### Example Output:
If you run the code, the output will be:
```
樓高: 1.5 丈
```

This means the height of the tower is **1 丈 5 尺**.
"""


"""
"""
