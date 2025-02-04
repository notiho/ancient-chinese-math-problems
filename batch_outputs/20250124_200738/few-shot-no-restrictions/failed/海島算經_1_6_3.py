"""
今有望清淵，淵下有白石。偃矩岸上，令句高三尺。斜望水岸，入下股四尺五寸。望白石，入下股二尺四寸。又設重矩于上，其間相去四尺。更從句端斜望水岸，入上股四尺。以望白石，入上股二尺二寸。問水深幾何？
術曰：置望水上下股相減，餘以乘望石上股為上率。又以望石上下股相減，餘以乘望水上股為下率。兩率相減，餘以乘矩間為實；以二差相乘為法。實如法而一，得水深。
答曰： a丈 。
"""

"""
This is a classic problem involving geometry and proportional reasoning to calculate the depth of water based on observations using a measuring tool (偃矩, a carpenter's square). Let's translate the problem and solution into Python code.

---

### Problem Breakdown:
1. **Given:**
   - A carpenter's square is placed on the bank with the vertical leg (句) 3 chi high.
   - Observations are made at two levels:
     - **Lower level:**
       - Looking at the water's edge, the horizontal leg (股) extends 4 chi 5 cun.
       - Looking at the white stone, the horizontal leg (股) extends 2 chi 4 cun.
     - **Upper level:**
       - The second carpenter's square is placed 4 chi above the first.
       - Looking at the water's edge, the horizontal leg (股) extends 4 chi.
       - Looking at the white stone, the horizontal leg (股) extends 2 chi 2 cun.
   - The distance between the two carpenter's squares is 4 chi.

2. **Question:**
   - What is the depth of the water?

3. **Procedure:**
   - Subtract the upper and lower 股 values for observing the water's edge. Multiply the difference by the 股 value for observing the white stone at the upper level to get the **upper ratio**.
   - Subtract the upper and lower 股 values for observing the white stone. Multiply the difference by the 股 value for observing the water's edge at the upper level to get the **lower ratio**.
   - Subtract the two ratios. Multiply the result by the distance between the two carpenter's squares to get the **numerator**.
   - Multiply the two 股 differences (for water's edge and white stone) to get the **denominator**.
   - Divide the numerator by the denominator to get the depth of the water.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Measurements (in chi and cun)
句高 = 3  # Vertical leg height in chi
矩間 = 4  # Distance between the two carpenter's squares in chi

# Lower level observations
望水下股 = 4 + Fraction(5, 10)  # 4 chi 5 cun
望石下股 = 2 + Fraction(4, 10)  # 2 chi 4 cun

# Upper level observations
望水上股 = 4  # 4 chi
望石上股 = 2 + Fraction(2, 10)  # 2 chi 2 cun

# Step 1: Calculate the upper ratio
望水股差 = 望水上股 - 望水下股
上率 = 望水股差 * 望石上股

# Step 2: Calculate the lower ratio
望石股差 = 望石上股 - 望石下股
下率 = 望石股差 * 望水上股

# Step 3: Calculate the numerator (實)
率差 = 上率 - 下率
實 = 率差 * 矩間

# Step 4: Calculate the denominator (法)
法 = 望水股差 * 望石股差

# Step 5: Calculate the depth of the water
水深 = Fraction(實, 法)

# Convert to zhang (1 zhang = 10 chi)
水深丈 = 水深 / 10

# Output the result
a = 水深丈
print(f"水深為 {a} 丈。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Conversion:**
   - All measurements are converted into fractions of chi (1 chi = 10 cun) for precise calculations.
2. **Step-by-Step Calculation:**
   - The differences in 股 values for water's edge and white stone are calculated.
   - These differences are used to compute the upper and lower ratios.
   - The numerator and denominator are calculated based on the procedure described in the problem.
   - The depth of the water is obtained by dividing the numerator by the denominator.
3. **Output:**
   - The result is converted into 丈 (1 丈 = 10 尺) for the final answer.

---

### Example Output:
If you run the code, the result will be:

```
水深為 a 丈。
```

Where `a` is the calculated depth of the water in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: -6/5"""
