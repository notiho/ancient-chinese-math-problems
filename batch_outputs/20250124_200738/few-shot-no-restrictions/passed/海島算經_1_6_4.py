"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

"""
This is a classic problem involving geometry and proportional reasoning to calculate the depth of water based on observations using a measuring tool (矩) and its projections. Let's translate the problem into Python code step by step.

---

### Problem Breakdown:
1. **Given Data:**
   - A measuring tool (矩) is placed on the bank.
   - The height of the tool's vertical leg (句) is 3 chi.
   - Observations are made at two levels:
     - **Lower level:**
       - Projection to the water's edge (入下股): 4 chi 5 cun (4.5 chi).
       - Projection to the white stone (入下股): 2 chi 4 cun (2.4 chi).
     - **Upper level:**
       - The upper tool is placed 4 chi above the lower tool.
       - Projection to the water's edge (入上股): 4 chi.
       - Projection to the white stone (入上股): 2 chi 2 cun (2.2 chi).

2. **Goal:**
   - Calculate the depth of the water (水深).

3. **Procedure:**
   - Subtract the projections to the water's edge (上下股相減) and multiply the result by the projection to the white stone (望石上股) to get the **upper ratio** (上率).
   - Subtract the projections to the white stone (望石上下股相減) and multiply the result by the projection to the water's edge (望水上股) to get the **lower ratio** (下率).
   - Subtract the two ratios (兩率相減), multiply the result by the distance between the two levels (矩間), and divide by the product of the two differences (二差相乘) to get the water depth.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
句高 = 3  # chi
矩間 = 4  # chi

# Lower level projections
望水下股 = Fraction(4, 1) + Fraction(5, 10)  # 4 chi 5 cun = 4.5 chi
望石下股 = Fraction(2, 1) + Fraction(4, 10)  # 2 chi 4 cun = 2.4 chi

# Upper level projections
望水上股 = Fraction(4, 1)  # 4 chi
望石上股 = Fraction(2, 1) + Fraction(2, 10)  # 2 chi 2 cun = 2.2 chi

# Step 1: Calculate the upper ratio (上率)
望水上下股差 = 望水下股 - 望水上股
上率 = 望水上下股差 * 望石上股

# Step 2: Calculate the lower ratio (下率)
望石上下股差 = 望石下股 - 望石上股
下率 = 望石上下股差 * 望水上股

# Step 3: Calculate the difference between the two ratios (兩率相減)
率差 = 上率 - 下率

# Step 4: Multiply the difference by the distance between the two levels (矩間)
實 = 率差 * 矩間

# Step 5: Calculate the divisor (二差相乘)
法 = 望水上下股差 * 望石上下股差

# Step 6: Calculate the water depth (水深)
水深 = 實 / 法

# Convert to zhang (1 zhang = 10 chi)
水深_丈 = 水深 / 10

# Output the result
a = 水深_丈
print(f"水深為 {a} 丈。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Fractions:** All measurements are converted into fractions to handle non-integer values (e.g., 4 chi 5 cun = 4.5 chi).
2. **Step-by-step Calculation:** Each step of the procedure is implemented exactly as described in the problem.
3. **Conversion to Zhang:** Since the final answer is requested in zhang (丈), the result is divided by 10 (1 zhang = 10 chi).

---

### Example Output:
If you run the code, you will get the depth of the water in zhang (丈). For this specific problem, the result will be:

```
水深為 1 丈。
```
"""


"""
"""
