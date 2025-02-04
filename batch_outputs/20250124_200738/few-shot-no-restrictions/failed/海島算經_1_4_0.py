"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
This is a classic ancient Chinese geometry problem involving similar triangles and proportional reasoning to calculate the height of a tower (樓高). Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given:**
   - A mountain with a slope (偃矩山上).
   - The height of the first triangle's vertical leg (句高) is 6 尺.
   - The horizontal distance (入下股) from the first observation point to the base of the tower is 1 丈 2 尺 (12 尺).
   - The horizontal distance (入上股) from the second observation point to the base of the tower is 1 丈 1 尺 4 寸 (11 尺 4 寸 = 11.4 尺).
   - The distance between the two observation points (矩閒) is 3 丈 (30 尺).
   - A small pole (小表) is placed at the intersection of the extended lines, and the horizontal distance (入小表) from the third observation point to the top of the tower is 8 寸 (0.8 尺).

2. **Procedure:**
   - Subtract the two horizontal distances (上下股相減) to find the divisor (法).
   - Multiply the distance between the observation points (矩閒) by the lower horizontal distance (以下股乘之), then divide by the divisor to find the height of the first triangle (如句高而一).
   - Multiply the result by the horizontal distance to the small pole (入小表乘之) to find the dividend (實).
   - Divide the dividend by the divisor to find the height of the tower (樓高).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = 6  # Height of the first triangle's vertical leg in 尺
入下股 = 12  # Horizontal distance from the first observation point to the base of the tower in 尺
入上股 = 11 + Fraction(4, 10)  # Horizontal distance from the second observation point to the base of the tower in 尺 (11 尺 4 寸)
矩閒 = 30  # Distance between the two observation points in 尺
入小表 = Fraction(8, 10)  # Horizontal distance to the small pole in 尺 (8 寸)

# Step 1: Calculate the divisor (上下股相減)
法 = 入下股 - 入上股

# Step 2: Calculate the height of the first triangle (如句高而一)
第一三角形高 = (矩閒 * 入下股) / 法

# Step 3: Multiply by the horizontal distance to the small pole (入小表乘之)
實 = 第一三角形高 * 入小表

# Step 4: Divide by the divisor to find the height of the tower (實如法而一)
樓高 = 實 / 法

# Convert the result to 丈 for the final answer
樓高_丈 = 樓高 / 10  # 1 丈 = 10 尺

# Output the result
a = 樓高_丈
print(f"樓高為 {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Values:** All measurements are converted into 尺 for consistency. For example, 1 丈 = 10 尺, and 1 寸 = 0.1 尺.
2. **Divisor (法):** The difference between the two horizontal distances (入下股 - 入上股).
3. **First Triangle Height:** Using the formula `(矩閒 * 入下股) / 法`.
4. **Dividend (實):** Multiply the first triangle height by the horizontal distance to the small pole (入小表).
5. **Tower Height (樓高):** Divide the dividend by the divisor to get the final height of the tower in 尺, then convert it to 丈.

---

### Example Output:
If you run the code, it will calculate the height of the tower in 丈. For this specific problem, the answer will be approximately:

```
樓高為 a 丈
```
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 80"""
