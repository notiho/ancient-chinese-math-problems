"""
今有登山望樓，樓在平地。偃矩山上，令句高六尺。從句端斜望樓足，入下股一丈二尺。又設重矩于上，令其間相去三丈。更從句端斜望樓足，入上股一丈一尺四寸。又立小表于入股之會，復從句端斜望樓岑端，入小表八寸。問樓高幾何？
術曰：上下股相減，餘為法；置矩閒，以下股乘之，如句高而一。所得，以入小表乘之，為實。實如法而一，即是樓高。
答曰： a丈 。
"""

"""
This is a classic ancient Chinese geometry problem involving similar triangles and proportional reasoning. Let's break it down step by step and translate it into Python code.

### Problem Description:
- A person is standing on a mountain and looking at a tower on flat ground.
- A right triangle is formed with the mountain slope (hypotenuse), the height of the mountain (opposite side), and the base (adjacent side).
- The problem involves multiple observations and setups:
  1. The height of the mountain (句高) is 6 chi.
  2. From the top of the mountain, the observer looks at the base of the tower. The base of the triangle (下股) is 1 zhang 2 chi (12 chi).
  3. A second observation is made from a point 3 zhang (30 chi) higher up the slope. The base of the triangle (上股) is now 1 zhang 1 chi 4 cun (11.4 chi).
  4. A small pole (小表) is placed at the intersection of the slopes. From the top of the mountain, the observer looks at the top of the tower, and the base of the triangle (入小表) is 8 cun (0.8 chi).
- The goal is to calculate the height of the tower (樓高).

### Procedure:
1. Subtract the lower base (下股) from the upper base (上股) to get the difference (法).
2. Multiply the difference by the distance between the two observation points (矩閒, 3 zhang = 30 chi).
3. Divide the result by the height of the mountain (句高) to get a proportional value.
4. Multiply this proportional value by the base of the small pole (入小表, 0.8 chi).
5. Divide the result by the difference (法) to get the height of the tower.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = 6  # Height of the mountain in chi
下股 = 12  # Lower base in chi (1 zhang 2 chi = 12 chi)
上股 = 11 + Fraction(4, 10)  # Upper base in chi (1 zhang 1 chi 4 cun = 11.4 chi)
矩閒 = 30  # Distance between observation points in chi (3 zhang = 30 chi)
入小表 = Fraction(8, 10)  # Base of the small pole in chi (8 cun = 0.8 chi)

# Step 1: Subtract the lower base from the upper base to get the difference (法)
法 = 下股 - 上股

# Step 2: Multiply the difference by the distance between the observation points
實 = 矩閒 * 法

# Step 3: Divide the result by the height of the mountain
比例值 = Fraction(實, 句高)

# Step 4: Multiply this proportional value by the base of the small pole
樓高_實 = 比例值 * 入小表

# Step 5: Divide the result by the difference (法) to get the height of the tower
樓高 = Fraction(樓高_實, 法)

# Convert the result to zhang for the final answer
a = 樓高 / 10  # Convert chi to zhang (1 zhang = 10 chi)

# Output the result
print(f"樓高為 {a} 丈。")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Fractions**: The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values like 11.4 chi and 0.8 chi.
2. **Units**: All values are converted to chi for consistency, and the final result is converted back to zhang (1 zhang = 10 chi).
3. **Step-by-step Calculation**: The code follows the procedure described in the problem, ensuring each step is implemented correctly.

### Final Answer:
The height of the tower (`樓高`) will be output in zhang.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 2/5"""
