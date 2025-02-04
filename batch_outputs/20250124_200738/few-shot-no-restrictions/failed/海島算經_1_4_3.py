"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
This is a classic ancient Chinese problem involving geometry and proportional reasoning to calculate the height of a tower (樓高) based on observations from a mountain. Let's translate the procedure into Python code step by step.

---

### Problem Breakdown:
1. **Given:**
   - A mountain with a right triangle (偃矩) where the vertical leg (句) is 6 chi (尺).
   - From the top of the mountain, the observer looks down at the base of the tower (樓足). The horizontal distance (下股) is 1 zhang 2 chi (12 chi).
   - A second observation is made from a point 3 zhang (30 chi) higher up the mountain. The new horizontal distance (上股) is 1 zhang 1 chi 4 cun (11 chi 4 cun = 11.4 chi).
   - A small pole (小表) is placed at the intersection of the horizontal distances, and the observer looks at the top of the tower (樓岑端). The horizontal distance to the small pole is 8 cun (0.8 chi).

2. **Question:**
   - What is the height of the tower (樓高)?

3. **Procedure:**
   - Subtract the upper horizontal distance (上股) from the lower horizontal distance (下股) to get the divisor (法).
   - Multiply the difference by the distance between the two observation points (矩閒 = 30 chi).
   - Divide the result by the height of the mountain's vertical leg (句高 = 6 chi).
   - Multiply the result by the distance to the small pole (入小表 = 0.8 chi).
   - Divide by the divisor (法) to get the height of the tower.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = 6  # Vertical leg of the mountain (chi)
下股 = 12  # Lower horizontal distance (chi)
上股 = Fraction(114, 10)  # Upper horizontal distance (11 chi 4 cun = 11.4 chi)
矩閒 = 30  # Distance between the two observation points (chi)
入小表 = Fraction(8, 10)  # Distance to the small pole (8 cun = 0.8 chi)

# Step 1: Calculate the divisor (法)
法 = 下股 - 上股

# Step 2: Multiply 矩閒 by 下股 and divide by 句高
差距 = 矩閒 * 法 / 句高

# Step 3: Multiply the result by 入小表
實 = 差距 * 入小表

# Step 4: Divide by 法 to get the height of the tower
樓高 = 實 / 法

# Convert to zhang (1 zhang = 10 chi)
樓高_丈 = 樓高 / 10

# Output the result
a = 樓高_丈
print(f"樓高: {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Fractions:** The `Fraction` class is used to handle non-integer values (e.g., 11.4 chi and 0.8 chi) precisely.
2. **Step-by-step calculations:** Each step of the procedure is implemented as described in the problem.
3. **Unit conversion:** The final result is converted from chi to zhang (1 zhang = 10 chi) for the answer.

---

### Example Output:
If you run the code, it will calculate the height of the tower (樓高) in zhang. The result will be stored in `a`.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 2/5"""
